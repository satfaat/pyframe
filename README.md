<style>
    body { 
        background-color: hsl(250, 50%, 5%);
        color: hwb(177 90% 0%);
    }
    *, *::before, *::after {
        box-sizing:border-box;
        -moz-box-sizing: border-box; 
        -webkit-box-sizing: border-box;
    }
    .clearfix::after, .row::after {
        content: "";
        display: table;
        clear: both;
    }
    .content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 10px;
        box-shadow: 0 1px 3px rgba(14, 9, 9, 0.5), 0 1px 2px rgba(0, 0, 0, 0.7);
        border-radius: 30px;
     }
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        grid-gap: 1rem;
        padding: 0 1rem;
    }
</style>

# prj.name = web.py web.server

- <a href="#installation">installation</a>
    - [start](#start)
    - [end](#end)
        - [for linux](#for_linux)
        - [for Microsoft Windows](#for_windows)
- [flask](#flask)


<section class="content">

### installation {#installation}
```
sudo apt install python3-venv
python -m venv .venv
# .venvfl
# .venvfapi
# .wget
```

```bash
mkdir -p ~/src/snap && cd ~/src/snap
mkvirtualenv snap -i flask
```
```bash
mkdir app
touch app/{__init__,app,config,main,views}.py
```

```bash
pip list # to check what we have
pip install -r requirements.txt
pip install -U pylint
python -m pip install --upgrade pip
```

<div class="grid">
<article>

### Start{#start}
```
.venv\Scripts\activate  # for powershell
source .venv/Scripts/activate  # for windows wth bash
source d:/devgit/pytest/.venv/Scripts/activate
source .venv/bin/activate
```

#### FLASK {#flask}
- [flask host](http://127.0.0.1:5000/)

<div class="grid"><article>

##### Windows:
```
cd D:\devgit\flask

set FLASK_APP=frun.py
set FLASK_DEBUG=1
set FLASK_ENV=development
flask run  # start off in app
python app.py  # start off in __main__
```

###### powerShell
```
$env:FLASK_APP = "webapp"
```

</article><article>

##### Linux
```
export FLASK_APP=flasky.py
export FLASK_DEBUG=1
export FLASK_ENV=development
flask run
```
</article></div>

</article>
<article>

### End {#end}
    `deactivate`
</article></div></section>