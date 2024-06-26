from datetime import datetime
from fastapi import APIRouter, Query, Request, status
from fastapi.responses import JSONResponse, RedirectResponse

from dtos.alterar_cliente_dto import AlterarClienteDTO
from dtos.alterar_senha_dto import AlterarSenhaDTO
from models.cliente_model import Cliente
from models.item_pedido_model import ItemPedido
from models.pedido_model import Pedido
from repositories.cliente_repo import ClienteRepo
from repositories.item_pedido_repo import ItemPedidoRepo
from repositories.pedido_repo import PedidoRepo
from repositories.produto_repo import ProdutoRepo
from util.auth import conferir_senha, obter_hash_senha
from util.cookies import (
    adicionar_mensagem_erro,
    adicionar_mensagem_sucesso,
    excluir_cookie_auth,
)
from util.templates import obter_jinja_templates

router = APIRouter(prefix="/cliente")
templates = obter_jinja_templates("templates/cliente")


@router.get("/pedidos")
async def get_pedidos(request: Request):
    return templates.TemplateResponse(
        "pages/pedidos.html",
        {"request": request},
    )


@router.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse(
        "pages/cadastro.html",
        {
            "request": request,
        },
    )


@router.post("/post_cadastro", response_class=JSONResponse)
async def post_cadastro(request: Request, alterar_dto: AlterarClienteDTO):
    id = request.state.cliente.id
    cliente_data = alterar_dto.model_dump()
    response = JSONResponse({"redirect": {"url": "/cliente/cadastro"}})
    if ClienteRepo.alterar(Cliente(id, **cliente_data)):
        adicionar_mensagem_sucesso(response, "Cadastro alterado com sucesso!")
    else:
        adicionar_mensagem_erro(
            response, "Não foi possível alterar os dados cadastrais!"
        )
    return response


@router.get("/senha")
async def get_senha(request: Request):
    return templates.TemplateResponse(
        "pages/senha.html",
        {"request": request},
    )


@router.post("/post_senha", response_class=JSONResponse)
async def post_senha(request: Request, alterar_dto: AlterarSenhaDTO):
    email = request.state.cliente.email
    cliente_bd = ClienteRepo.obter_por_email(email)
    nova_senha_hash = obter_hash_senha(alterar_dto.nova_senha)
    response = JSONResponse({"redirect": {"url": "/cliente/senha"}})
    if not conferir_senha(alterar_dto.senha, cliente_bd.senha):
        adicionar_mensagem_erro(response, "Senha atual incorreta!")
        return response
    if ClienteRepo.alterar_senha(cliente_bd.id, nova_senha_hash):
        adicionar_mensagem_sucesso(response, "Senha alterada com sucesso!")
    else:
        adicionar_mensagem_erro(response, "Não foi possível alterar sua senha!")
    return response


@router.get("/sair", response_class=RedirectResponse)
async def get_sair(request: Request):
    if request.state.cliente:
        ClienteRepo.alterar_token(request.state.cliente.email, "")
    response = RedirectResponse("/", status.HTTP_303_SEE_OTHER)
    excluir_cookie_auth(response)
    adicionar_mensagem_sucesso(response, "Saída realizada com sucesso!")
    return response


@router.get("/carrinho")
async def get_carrinho(request: Request, id_produto: int = Query(0)):
    if id_produto:
        pedido_carrinho = PedidoRepo.obter_por_estado(request.state.cliente.id, 1)
        if pedido_carrinho == None:
            pedido_carrinho = Pedido(0, datetime.now(), 0, request.state.cliente.endereco, 1, request.state.cliente.id)
            pedido_carrinho = PedidoRepo.inserir(pedido_carrinho)
        
        qtde = ItemPedidoRepo.obter_quantidade_por_produto(pedido_carrinho.id, id_produto)

        if qtde == 0:
            produto = ProdutoRepo.obter_um(id_produto)
            item_pedido = ItemPedido(pedido_carrinho.id, id_produto, produto.nome, produto.preco, 1, 0)
            ItemPedidoRepo.inserir(item_pedido)
        else:
            ItemPedidoRepo.aumentar_quantidade_produto(pedido_carrinho.id, id_produto)

    pedido_carrinho = PedidoRepo.obter_por_estado(request.state.cliente.id, 1)
    if pedido_carrinho:
        itens_pedido = ItemPedidoRepo.obter_por_pedido(pedido_carrinho.id)
    else:
        itens_pedido = []

    return templates.TemplateResponse(
        "pages/carrinho.html",
        {"request": request, "itens": itens_pedido},
    )