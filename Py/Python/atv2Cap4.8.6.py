def converter_hora(hora):
    horas = int(hora[:2])
    minutos = int(hora[-2:])
    periodo = "AM"

    if horas >= 12:
        horas -= 12
        periodo= 'PM'

        return horas, minutos, periodo

def saida (horas, minutos, periodo):
    print(f"{horas}:{minutos} {periodo}")

for i in range(6):
    saida(*converter_hora(input("Digite uma hora:")))
