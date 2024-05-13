vinhos = {"A": 35, "B": 55, "C": 45, "D":65, "E":75}
filtro = lambda tupla : tupla[1] > 50
vinhos_caros = list(filter(filtro, vinhos.items()))

print(vinhos_caros)