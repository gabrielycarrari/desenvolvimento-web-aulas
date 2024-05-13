import re

usuario = str(input("Digite um nome de usuário: "))
senha = str(input("Digite uma senha: "))

usuario_limpo = re.sub(r"\W", "", usuario)
senha_limpa = re.sub(r"\W", "", senha)

print(f"Usuário limpo: {usuario_limpo}")
print(f"Senha limpa: {senha_limpa}")