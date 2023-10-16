class Bola:
    def __init__(self, cor="unknown", circuferencia= 0, material="unknown"):
        self.c = cor
        self.ci= circuferencia
        self.m = material

    def trocaCor(self):
        trocar = input("deseja trocar de cor {}? [s/n]:".format(self.c))
        trocar = trocar[0].lower()


        if trocar == "s":
            novacor = input("\n> nova cor: ")
            self.c = novacor
        else:
            print("a cor continua {}".format(self.c))

    def monstrarcor(self):
        print("\n A nova cor é {}".format(self.c))


def main():
    bola1 = Bola("verde", 5, "metal")

    while True:
        bola1.monstrarcor()
        bola1.trocaCor()

        continuar = input("Continuar? [s/n]:")
        continuar = continuar[0].lower()
        if continuar == "n":
            break
    
    bola1.monstrarcor()


main()          