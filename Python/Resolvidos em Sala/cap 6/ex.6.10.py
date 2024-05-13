frase = input("Digite uma frase: ")

palavras = frase.split()
tamanhos = list(map(lambda p: len(p), palavras))

print(tamanhos)