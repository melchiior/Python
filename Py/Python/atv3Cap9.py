class Bomba_combustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tC= tipoCombustivel
        self.vL= valorLitro
        self.qC= quantidadeCombustivel

    def abastecerPorValor(self):
        abastecerValor = int(input("qual o valor que deseja colocar? "))
        self.qC = self.qC - abastecerValor
    
    def abastecerPorLitro(self):
        abastecerLitro = int(input("Quantos litros deseja colocar? "))
        self.qC = self.qC - abastecerLitro
    def alterarValor(self):
        alterarValor = input("deseja alterar o valor?  [s/n] ")
        alterarValor = alterarValor[0].lower()

        if alterarValor == "s":
            novo_valor = input("\nDigite o novo valor: ")
            self.vL = novo_valor
        else:
            print("O valor continua {}".format(self.vL))

    def alterarCombustivel(self):
        alterarC = input("Deseja alterar o combustivel? {} [s/n]".format(self.tC))
        alterarC = alterarC[0].lower

        if alterarC == "s":
            novo_combustivel = input("\nQual combustivel deseja?: ")
            self.tC = novo_combustivel
        else:
            print("O mesmo combustivel continua. {} ".format(self.tC))

    def alterarQuantidadeCobustivel(self):
        alterarQuantidade = input("Deseja alterar a quantidade de combustivel? {} [s/n]".format(self.qC))
        alterarQuantidade = alterarQuantidade[0].lower()

        if alterarQuantidade == "s":
            nova_quantidade = input("\nDigite a quantidade que deseja: ")
            self.qC = nova_quantidade
        else:
            print("A quantidade contianua. {}".format(self.qC))

def main():
    bomba1 = Bomba_combustivel("Gasolina", 4.19, 50)

    while True:
        bomba1.abastecerPorValor()
        bomba1.abastecerPorLitro()
        bomba1.alterarValor()
        bomba1.alterarCombustivel()
        bomba1.alterarQuantidadeCobustivel()

        continuar = input("Deseja reabastecer? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break
    
main()