with open("dados.txt", "w", encoding="utf-8") as arquivo:
    for i in range(10):
        arquivo.write(f"Linha {i+1}\n")