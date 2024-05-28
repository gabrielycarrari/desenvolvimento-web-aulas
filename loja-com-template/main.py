from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from repositories.produto_repo import ProdutoRepo
from routes import main_routes, cliente_routes

ProdutoRepo.criar_tabela()
ProdutoRepo.inserir_produtos_json("sql/produtos.json")

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(main_routes.router)
app.include_router(cliente_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)