qtd_com_o = 0
qtd_com_a = 0

# while len(palavras) != 5:
frase = input("Digite uma frase: ")
palavras = frase.split()

for palavra in palavras:
    if palavra.endswith("o"): qtd_com_o += 1
    if palavra.endswith("a"): qtd_com_a += 1

print(palavras)
print(f"\nQuantidade de palavra(s) termidada(s) em o: {qtd_com_o}")
print(f"\nQuantidade de palavra(s) termidada(s) em a: {qtd_com_a}")

