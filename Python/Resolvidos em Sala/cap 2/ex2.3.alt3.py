letra = str(input("Digite uma letra: "))
vogais = "aeiouAEIOU"

if letra in vogais:
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")
