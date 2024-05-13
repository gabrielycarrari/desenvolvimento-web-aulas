letra = str(input("Digite uma letra: "))
condicoes_vogal = [letra == "a", letra == "e", letra == "i", letra == "o", letra == "u", letra == "A", letra == "E", letra == "I", letra == "O", letra == "U"]

if all(condicoes_vogal):
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} é uma consoante.")