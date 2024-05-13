import datetime
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
agora = datetime.datetime.now()

hora_24 = agora.strftime("%H:%M")
hora_12 = agora.strftime("%I:%M %p")
dia_semana = agora.strftime("%A")
data_formatada = agora.strftime("%d/%m/%Y")

print("Hora em 24 horas: ", hora_24)
print("Hora em 12 horas: ", hora_12)

print(f"São {hora_24}h do dia {data_formatada}, que é {dia_semana}.")
print(agora.strftime("%A, %d de %B de %Y, %H:%mh."))



