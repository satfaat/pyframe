## installation

`python -m venv .venv`
`sudo apt install python3-venv`

```
mkdir -p ~/src/snap && cd ~/src/snap
mkvirtualenv snap -i flask
```
mkdir app
touch app/{__init__,app,config,main,views}.py

### Start
`.venv\Scripts\activate`
`source d:/devgit/pytest/.venv/Scripts/activate`
`source .venv/bin/activate`


`pip install -r requirements.txt`
`pip install -U pylint`

### End
    `deactivate`

#### for Linux
`(venv) $ export FLASK_APP=flasky.py`
`(venv) $ export FLASK_DEBUG=1`
#### for Microsoft Windows:
`(venv) $ set FLASK_APP=flasky.py`
`(venv) $ set FLASK_DEBUG=1`

## FLASK
http://127.0.0.1:5000/
win:
```
cd D:\devgit\flask

set FLASK_APP=hello.py
flask run  # start off in app
python app.py  # start off in __main__
```
### Linux
export FLASK_APP=flsky.py
export FLASK_ENV=development
flask run

### Win
set FLASK_APP=flsky.py
set FLASK_ENV=development
flask run

### app


## shell


## sql
```
import sqlalchemy
sqlalchemy.__version__
```


## Links
[palletsprojects](https://flask.palletsprojects.com/en/1.1.x/)
[flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
[]()

## VSC
Ctrl+/  # comment all rows


