// go
window.onload = init;

    function init() {
        addSticky();
    }

// notetoself


function addSticky(){
    let button = document.querySelector('#add_button');
    button.onclick = createSticky;

    let stickiesArray = getStickiesArray(); //arr
    for (let index in stickiesArray){ // 0-11
        let key = stickiesArray[index];
        let value = localStorage[key];
        addStickyToDOM(key, value);
    }
}


function addStickyToDOM(key, value) {
    let stickies = document.querySelector("#stickies");
    let sticky = document.createElement("li");
    sticky.setAttribute("id", key);

    let span = document.createElement("span");
    span.setAttribute("class", "sticky");
    span.innerHTML = value;
    sticky.appendChild(span);
    stickies.appendChild(sticky);

    // delete by id
    sticky.ondrag = deleteSticky;
}


function createSticky() {
    let stickiesArray = getStickiesArray();
    let currentDate = new Date();
    let key = "sticky_" + currentDate.getTime();
    let value = document.querySelector("#note_text").value;

    localStorage.setItem(key, value);
    stickiesArray.push(key);
    localStorage.setItem("stickiesArray", JSON.stringify(stickiesArray));

    addStickyToDOM(key, value);
}

function getStickiesArray() {
    let stickiesArray = localStorage.getItem("stickiesArray");
    if (!stickiesArray) {
        stickiesArray = [];
        localStorage.setItem("stickiesArray", JSON.stringify(stickiesArray));
    } else {
        stickiesArray = JSON.parse(stickiesArray);
    }
    return stickiesArray;
}

function deleteSticky(e) {
    let key = e.target.id;
    if (e.target.tagName.toLowerCase() == "span") {
        key = e.target.parentNode.id;
    }
    let stickiesArray = getStickiesArray();
    if (stickiesArray) {
        for (let index in stickiesArray){
            if (key == stickiesArray[index]){
                stickiesArray.splice(index,1);
            }
        }
        localStorage.removeItem(key);
        localStorage.setItem("stickiesArray", JSON.stringify(stickiesArray));
        removeStickyFromDOM(key);
    }
}

function removeStickyFromDOM(key) {
    let sticky = document.querySelector('#'+key);
    sticky.parentNode.removeChild(sticky);
}