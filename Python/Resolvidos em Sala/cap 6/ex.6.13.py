lista1 = [12, 4, 18, 7, 3]
lista2 = [8, 13, 2, 16, 10]

medias = [(n + n2)/2 for n, n2 in zip(lista1, lista2)]

print(medias)