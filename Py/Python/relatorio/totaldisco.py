usado = {}
contador = 0
capacidade = 0
percentual = 0.0

def calcular_total():
    usototal = sum(usado.values()) / 1024 / 1024
    return usototal

def calcular_percentual(espaco, total):
    razao = (espaco / total * 100) / 1024 / 1024
    return razao

with open('usuarios.txt', 'r') as f:
    linhas = f.readlines()
    for linha in linhas:
        (usuario, uso) = linha.split()
        usado[usuario] = float(uso)

capacidade = calcular_total()

with open('relatorio.txt', 'w+', encoding='utf8') as r:
    r.write("ACME Inc. \t\t\t\t Uso do espaço em disco pelos usuários\n\n")
    r.write("-"*80)
    r.write("\n\n\n Nr. \t\t Usuário \t\t Espaço Utilizado \t % do uso\n\n")

    for usuario, uso in usado.items():
        contador += 1
        percentual = calcular_percentual(uso, capacidade)
        r.write(f"\t0{contador}\t\t{usuario}:\t\t{uso/1024/1024:>9.2f} MB\t\t\t{percentual:>4.2f}%\n")

    r.write("\n Total usado em disco:\t\t {:>2.2f} MB".format(capacidade))
    r.write("\n Média usada em disco:\t\t {:>7.2f} MB".format(capacidade/contador))
    r.close()
