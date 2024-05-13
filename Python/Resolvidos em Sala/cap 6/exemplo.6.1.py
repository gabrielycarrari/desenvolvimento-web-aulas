numeros=[1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)

quadrados_pares = [x**2 for x in numeros if x%2==0]
print(quadrados_pares)

vinhos = {"A": 35, "B": 55, "C": 45, "D":65, "E":75}
vinhos_caros = {k: v for k, v in vinhos.items() if v > 50}
print(vinhos_caros)