- <a href="#installation">installation</a>
    - [start](#start)
    - [end](#end)
        - [for linux](#for_linux)
        - [for Microsoft Windows](#for_windows)
- [flask](#flask)
- [fastapi](#fastapi)
- [](#)


## installation {#installation}
```
sudo apt install python3-venv
python -m venv .venv
```

```
mkdir -p ~/src/snap && cd ~/src/snap
mkvirtualenv snap -i flask
```
```bash
mkdir app
touch app/{__init__,app,config,main,views}.py
```

### Start {#start}
```
.venv\Scripts\activate
source d:/devgit/pytest/.venv/Scripts/activate
source .venv/bin/activate
```

```
pip install -r requirements.txt
pip install -U pylint
python -m pip install --upgrade pip
```

### End {#end}
    `deactivate`

#### for Linux {#for_linux}
```
(venv) $ export FLASK_APP=flasky.py
(venv) $ export FLASK_DEBUG=1
```

#### for Microsoft Windows: {#for_windows}
```
(venv) $ set FLASK_APP=flasky.py
(venv) $ set FLASK_DEBUG=1
```

## FLASK {#flask}
[flask host](http://127.0.0.1:5000/)


## FastAPI {#fastapi}

```
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

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [local docs](http://127.0.0.1:8000/docs)
- [localhost](http://127.0.0.1:8000/)
- [local redoc](http://127.0.0.1:8000/redoc)
- [tutorial](https://fastapi.tiangolo.com/tutorial/)
- [async](https://fastapi.tiangolo.com/async/#in-a-hurry)
- [](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864)


### Windows:
```
cd D:\devgit\flask

set FLASK_APP=frun.py
set FLASK_DEBUG=1
set FLASK_ENV=development
flask run  # start off in app
python app.py  # start off in __main__
```
### Linux
```
export FLASK_APP=flsky.py
export FLASK_DEBUG=1
export FLASK_ENV=development
flask run
```

### powerShell
```
$env:FLASK_APP = "webapp"
```

## shell


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

