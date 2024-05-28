from fastapi import Body, FastAPI, Header, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ler_html import ler_html

app = FastAPI()

templates = Jinja2Templates(directory = "templates")
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contato")
def get_root(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.get("/cadastro")
def get_root(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.get("/entrar")
def get_root(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@app.get("/pedidos")
def get_root(request: Request):
    return templates.TemplateResponse("pedidos.html", {"request": request})

@app.get("/perfil")
def get_root(request: Request):
    return templates.TemplateResponse("perfil.html", {"request": request})

@app.get("/loja/{arquivo}")
def get_loja_arquivo(arquivo: str):
    response = HTMLResponse(ler_html(arquivo))
    return response