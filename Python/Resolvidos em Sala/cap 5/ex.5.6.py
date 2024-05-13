from typing import List



def adicionar(lista: List[int], novo_elemento: int):
    lista.append(novo_elemento)


idades = [22, 23, 45, 64, 12]
adicionar(idades, 25)
print(idades)