with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha  in arquivo.readlines():
        print(linha, end="")