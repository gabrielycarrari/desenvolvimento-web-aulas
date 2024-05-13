import random

sorteio = random.randint(1, 10)
palpite = int(input("Adivinhe o número sorteado: "))

if palpite == sorteio:
    print(f"Você acertou!")
elif palpite < sorteio:
    print(f"Você chutou baixo!")
else: 
    print(f"Você chutou alto!")
