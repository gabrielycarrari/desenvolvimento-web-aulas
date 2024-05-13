import random

opcoes = ["pedra", "papel", "tesoura"]
npc = random.choice(opcoes)

print("Opções:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")
resposta = int(input("Qual é a sua opção? "))

op_usuario = opcoes[resposta-1]
if npc == op_usuario:
    print("Empatou")

elif npc == "pedra" and op_usuario == "tesoura":
    print(f"Computador venceu com '{npc}' contra '{op_usuario}'.")
elif npc == "pedra" and op_usuario == "papel":
    print(f"Usuário venceu com '{op_usuario}' contra '{npc}'.")

elif npc == "papel" and op_usuario == "pedra":
    print(f"Computador venceu com '{npc}' contra '{op_usuario}'.")
elif npc == "papel" and op_usuario == "tesoura":
    print(f"Usuário venceu com '{op_usuario}' contra '{npc}'.")

elif npc == "tesoura" and op_usuario == "papel":
    print(f"Computador venceu com '{npc}' contra '{op_usuario}'.")
elif npc == "tesoura" and op_usuario == "pedra":
    print(f"Usuário venceu com '{op_usuario}' contra '{npc}'.")