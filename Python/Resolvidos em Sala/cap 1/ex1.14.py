nome_produto = input("Nome do produto: ")
preco_custo = float(input("Preço de custo: "))
preco_venda = float(input("Preço de venda: "))
qtde_estoque = int(input("Quantidade em estoque: "))
lucro_por_produto = preco_venda - preco_custo
lucro_total = qtde_estoque * lucro_por_produto

print(f"O lucro total é de R$ {lucro_total:.2f}.")
