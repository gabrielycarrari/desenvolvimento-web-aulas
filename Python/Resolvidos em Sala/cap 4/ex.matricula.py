import re

er_matricula = r'\d{4}[a-zA-Z]{2}\d{3}'
matricula = input("Digite sua matrícula: ")

# if re.fullmatch(er_matricula, matricula):
if re.match(er_matricula, matricula):
    print("Matrícula correta.")
else:
    print("Matrícula incorreta")