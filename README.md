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
    /*TEXT*/
</style>

# prj.name = web.py

- <a href="#installation">installation</a>
    - [start](#start)
    - [end](#end)
        - [for linux](#for_linux)
        - [for Microsoft Windows](#for_windows)
- [flask](#flask)
- [fastapi](#fastapi)
- [](#)

<section class="content">

## FLASK {#flask}
- [flask host](http://127.0.0.1:5000/)

### installation {#installation}
```
sudo apt install python3-venv
python -m venv .venv
# .venvfl
# .venvfapi
```

```
mkdir -p ~/src/snap && cd ~/src/snap
mkvirtualenv snap -i flask
```
```bash
mkdir app
touch app/{__init__,app,config,main,views}.py
```

```
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

<div class="grid"><article>

#### Windows:
```
cd D:\devgit\flask

set FLASK_APP=frun.py
set FLASK_DEBUG=1
set FLASK_ENV=development
flask run  # start off in app
python app.py  # start off in __main__
```
##### powerShell
```
$env:FLASK_APP = "webapp"
```

</article><article>

#### Linux
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
</article>
</div>


## FastAPI {#fastapi}
- [fast api](http://127.0.0.1:8000)

```bash
pip install fastapi
pip install uvicorn[standard]
```
```
uvicorn main:app --reload
uvicorn sql_app.main:app --reload
uvicorn app.main:app --reload --port 8080
```

- main: the file main.py (the Python "module").
- app: the object created inside of main.py with the line app = FastAPI().
- --reload: make the server restart after code changes. Only do this for development.


<details>
    <summary>links</summary>

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [local docs](http://127.0.0.1:8000/docs)
- [localhost](http://127.0.0.1:8000/)
- [local redoc](http://127.0.0.1:8000/redoc)
- [tutorial](https://fastapi.tiangolo.com/tutorial/)
- [async](https://fastapi.tiangolo.com/async/#in-a-hurry)
- [](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864)

</details>


## sql
```
import sqlalchemy
sqlalchemy.__version__
```
## mongo {#mongo}
[mongodb-python](https://www.mongodb.com/python)
```
python -m pip install pymongo
pip install pymongo
```

## Links {#links}
* [palletsprojects](https://flask.palletsprojects.com/en/1.1.x/)
* [flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* []()

## VSC
| command | description |
--- | --- 
| Ctrl+/  | # comment all rows |
| View > Command Palette or Ctrl+Shift+P | |

-[markdown](https://www.w3schools.io/file/markdown-checkbox-github/)

</section>