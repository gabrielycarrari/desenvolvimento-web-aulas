from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory = "templates")

@router.get("/pedidos")
def get_root(request: Request):
    return templates.TemplateResponse("pedidos.html", {"request": request})

@router.get("/perfil")
def get_root(request: Request):
    return templates.TemplateResponse("perfil.html", {"request": request})
