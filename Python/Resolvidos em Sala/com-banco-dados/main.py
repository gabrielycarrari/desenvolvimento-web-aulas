from os import system
from model.produto import Produto
from repo.produto import ProdutoRepo


ProdutoRepo.criar_tabela()

def mostrar_menu():
    print("\n--------------------")
    print("CADASTRO DE PRODUTOS")
    print("--------------------")
    print("1. Inserir")
    print("2. Listar")
    print("3. Alterar")
    print("4. Excluir")
    print("5. Detalhes")
    print("6. Sair")


def obter_opcao() -> int:
    opcao = int(input("Opção desejada: "))
    return opcao


def inserir():
    print("\n----------------")
    print("INSERIR PRODUTO")
    print("---------------")
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    estoque = int(input("Estoque: "))
    preco = float(input("Preço: "))
    p = Produto(None, nome, descricao, estoque, preco)
    ProdutoRepo.inserir(p)
    input("Pressione ENTER para prosseguir...")


def listar():
    print("\n----------------")
    print("LISTAR PRODUTOS")
    print("---------------")
    print("ID NOME")
    produtos = ProdutoRepo.obter_todos()
    for p in produtos:
        print(f"{p.id:02d} {p.nome}")
    input("\nPressione ENTER para prosseguir...")


def alterar():
    print("\n----------------")
    print("ALTERAR PRODUTO")
    print("---------------")
    id = int(input("Código: "))
    p = ProdutoRepo.obter_um(id)

    nome = input(f"Nome ({p.nome}): ")
    descricao = input(f"Descrição ({p.descricao}): ")
    estoque = int(input(f"Estoque ({p.estoque}): "))
    preco = float(input(f"Preço ({p.preco:.2f}): "))
    p = Produto(id, nome, descricao, estoque, preco)
    ProdutoRepo.alterar(p)
    input("Pressione ENTER para prosseguir...")


def excluir():
    print("\n----------------")
    print("EXCLUIR PRODUTO")
    print("---------------")
    id = int(input("Código: "))
    p = ProdutoRepo.obter_um(id)
    resposta = input(f"Deseja realmente excluir o produto {p.nome}? (S/N) ")
    if resposta.upper() == "S":
        ProdutoRepo.excluir(id)
    input("Pressione ENTER para prosseguir...")


def detalhar():
    print("\n----------------")
    print("DETALHAR PRODUTO")
    print("----------------")
    id = int(input("Código: "))
    p = ProdutoRepo.obter_um(id)
    print(f"Nome: {p.nome}")
    print(f"Descrição: {p.descricao}")
    print(f"Estoque: {p.estoque}")
    print(f"Preço: {p.preco}")
    input("Pressione ENTER para prosseguir...")


while True:
    system("cls")
    mostrar_menu()
    opcao = obter_opcao()
    system("cls")
    match(opcao):
        case 1: inserir()
        case 2: listar()
        case 3: alterar()
        case 4: excluir()
        case 5: detalhar()
        case 6: break
        case _: input("Opção inválida! Pressione ENTER para voltar ao menu...")

print("\nSistema de cadastro de produtos finalizado!")