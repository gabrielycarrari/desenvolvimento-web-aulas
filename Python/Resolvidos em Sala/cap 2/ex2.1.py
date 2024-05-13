numero = int(input("Digite um número inteiro: "))
eh_par = (numero % 2 == 0)
if eh_par:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")