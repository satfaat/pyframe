from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from pydantic import BaseModel

from .libra.helpers import *


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    data = {
        'template_name': 'index.html',
        'title': 'Home page',
        'page': 'index',
        'md_content': openfile('home.md')
    }
    return templates.TemplateResponse(
        data['template_name'],
        {'request': request, 'data': data}
    )


@app.get("/page/{page_name}")
async def page(request: Request ,page_name: str):
    data = {
        'template_name': 'index.html',
        "page": page_name,
        'md_content': openfile(page_name+'.md')
    }
    return templates.TemplateResponse(
        data['template_name'],
        {'request': request, 'data': data}
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
