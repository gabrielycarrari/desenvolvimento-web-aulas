from fastapi import Body, FastAPI, Header, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from ler_html import ler_html

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root():
    return "Olá, FastAPI!"

@app.get("/ola/{nome}")
def get_ola(nome: str):
    return f"Olá, {nome}!"

@app.get("/bomdia")
def get_bomdia(nome: str):
    return f"Bom dia, {nome}!"

@app.post("/boatarde")
def post_boatarde(nome: str = Body(embed=True)):
    return f"Boa tarde, {nome}!"

@app.get("/boanoite")
def get_boanoite(nome: str = Header()):
    return f"Boa noite, {nome}!"

@app.get("/navegador")
def get_navegador(user_agent: str = Header()):
    return f"Você está usando o navegador {user_agent}!"

@app.get("/header/{chave}/{valor}")
def get_header(response: Response, chave: str, valor: str):
    response.headers[chave] = valor
    return f"Você me mandou um cabeçalho personalizado"

@app.get("/html")
def get_html():
    html = """
        <h1>Olá, FastAPI</h1>
        <hr>
        <img src='/static/img/logotipo.svg' style='width=50%'>
    """
    response = HTMLResponse(html)
    return response

@app.get("/loja")
def get_loja():
    response = HTMLResponse(ler_html("index"))
    return response

@app.get("/loja/{arquivo}")
def get_loja_arquivo(arquivo: str):
    response = HTMLResponse(ler_html(arquivo))
    return response