soma = 0
for numero in range(2,101,2):
    soma += numero
    print(numero, end=", ")

print(f"\nA soma dos pares é {soma}.")