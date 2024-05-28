from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ler_html import ler_html
from repositories.produto_repo import ProdutoRepo

router = APIRouter()

templates = Jinja2Templates(directory = "templates")

@router.get("/html/{arquivo}")
def get_loja_arquivo(arquivo: str):
    response = HTMLResponse(ler_html(arquivo))
    return response

@router.get("/")
def get_root(request: Request):
    produtos = ProdutoRepo.obter_todos()
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})

@router.get("/contato")
def get_contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@router.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.get("/entrar")
def get_entrar(request: Request):
    return templates.TemplateResponse("entrar.html", {"request": request})

@router.get("/produto/{id:int}")
def get_produto(request: Request, id: int):
    produto = ProdutoRepo.obter_um(id)
    return templates.TemplateResponse("produto.html", {"request": request, "produto": produto})

@router.get("/buscar")
def get_root(request: Request, q:str):
    produtos = ProdutoRepo.obter_busca(q)
    return templates.TemplateResponse("buscar.html", {"request": request, "produtos": produtos})