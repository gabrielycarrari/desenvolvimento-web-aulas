valor_total = float(input("Valor total da venda: "))
percentual_desconto = float(input("Percentual de desconto: "))
percentual_imposto = float(input("Percentual de desconto: "))

preco_com_desconto = valor_total - valor_total * (percentual_desconto/100)
preco_final = preco_com_desconto - preco_com_desconto * (percentual_imposto/100)

print(f"O preço final é de R$ {preco_final:.2f}.")
