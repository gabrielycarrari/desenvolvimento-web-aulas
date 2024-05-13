numero_digitado = 0
soma = 0
qtde_numeros = 0

while numero_digitado >= 0:
    soma += numero_digitado    
    numero_digitado = int(input("Digite um núemro (-1 para sair): "))
    qtde_numeros +=1

media = soma/(qtde_numeros-1)

print(f"\nA média dos números é {media}.")