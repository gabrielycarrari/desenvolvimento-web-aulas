from datetime import datetime, timedelta

data_nascimento = datetime(2001, 10, 24)
data_atual = datetime.now()

diferenca = data_atual - data_nascimento

print(f"Você já viveu {diferenca.days} dias.")


sete_dias = timedelta(weeks=1)
data_futura = data_atual + sete_dias
print(data_futura)