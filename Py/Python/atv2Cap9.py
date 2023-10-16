class Quadrado:
    def __init__(self, tamanho_do_lado = 0):
        self.tl = tamanho_do_lado

    def mudar_valor_l(self):
        mudarValor = input("deseja mudar o valor do lado {}? [s/n]: ".format(self.tl))
        mudarValor = mudarValor[0].lower()

        if mudarValor == "s":
            novo_valor = int(input("\n novo valor do lado:"))
            self.tl = novo_valor
        else:
            print(" A cor continua. {}".format(self.tl))


    def retornar_valor(self):
        print("Deseja retornar o valor? [s/n]: ".format(self.tl))

    def calcular_area(self):
        area = self.tl * self.tl
        print(f"\nA area área do quadrado é {area:.2f} cm².")
    

def main():
    lado1 = Quadrado(4)

    while True:
        lado1.mudar_valor_l()
        lado1.retornar_valor()
        lado1.calcular_area()
        continuar = input("\n continuar? [s/n]")
        continuar = continuar[0].lower()
        if continuar == "n":
            break

main()