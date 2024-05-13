# palavras = []

# while len(palavras) != 5:
#     frase = input("Digite uma frase com 5 palavras: ")
#     palavras = frase.split()

# for palavra in palavras:
#     print(palavra)

# print(palavras)
# print(f"\nA média dos números é {media}.")

#############################################################
# Solução Prof

while True:
    frase = input("Digite uma frase com 5 palavras: ")
    palavras = frase.split()
    qtde_palavras = len(palavras)
    if qtde_palavras == 5:
        print("Parabéns! Você digitou corretamente. Palavras: ")
        for p in palavras:
            print(p)
        break
    else:
        print(f"Sua frase tem {qtde_palavras} palavras. Tente novamente...")