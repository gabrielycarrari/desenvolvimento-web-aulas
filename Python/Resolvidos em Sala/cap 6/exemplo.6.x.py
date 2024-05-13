# Faça um programa que percorra uma lista de 0 a 200 números e retorne os divisíveis por 3 e 5 ao mesmo tempo.

lista = list(range(201))

divisiveis = [n for n in lista if n%3 == 0 and n%5 == 0]

print(divisiveis)
