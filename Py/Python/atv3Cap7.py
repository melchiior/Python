usado = {}
contador = 0
capacidade = 0
percentual = 0.0

def calcualr_total():
    usototal = sum(usado.values()) / 1024 / 1024
    return usototal

def calcular_percentual(espaco, total):
    razao = (espaco / total * 100) / 1024 / 1024
    return razao

with open('usuarios.txt', 'r') as a:
    linhas = a.readlines()
    for linha in linhas:
        (usuario, uso) = linha.split()
        usado[usuario] = float(uso)

capacidade = calcualr_total()

with open('relatorio.txt', 'w+', encoding='utf8') as a:
    a.write("ACME Inc. \t\t\t\t Uso do espaço em disco pelos usuários\n\n")
    a.write("-"*80)
    a.write("\n\n\n Nr. \t\t Usuário \t\t Espaço Utilizado \t % do uso\n\n")

    for usuario, uso in usado.items():
        contador += 1
        percentual = calcular_percentual(uso, capacidade)
        a.write(f"\t0{contador}\t\t{usuario}:\t\t{uso/1024/1024:>9.2f} MB\t\t\t{percentual:>4.2f}%\n")
    
    a.write("\n Total usado em disco:\t\t {:>2.2f} MB".format(capacidade))
    a.write("\n Média usada em disco:\t\t {:>7.2f} MB".format(capacidade/contador))
    a.close()