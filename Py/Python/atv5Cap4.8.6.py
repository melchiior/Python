def contaDigito(n):
    return len( str(n) )
def exibe():
    n = int(input('Digite um inteiro: '))
    print(contaDigito(n), ' dígitos')
    
while True:
    exibe()