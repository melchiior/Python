meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']


def validade(data):
    if data[2] != '/' and data[5] != '/' and len(data) != 10:
        print('Data inválida!')
    else:
        mes = int(data[3:5])
        print(data[:2] + ' de ' + meses[mes - 1] + ' de ' + data[-4:])

validade(input("Digite uma data: "))

