class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Ponto(%s, %s)"% (repr(self.x), repr(self.y))
    
class Retangulo:
    def __init__(self, canto1 = 0, canto2 = 0):
            self.c1 = canto1
            self.c2 = canto2
        
    def centro(self):
        x_centro = float(self.c1.x) /2 + float(self.c2.x) /2
        y_centro = float(self.c1.y) /2 + float(self.c2.y) /2
        return Ponto(x_centro, y_centro)

x1 = input("Digite a coordenada X do canto inferior esquerdo: ")
y1 = input("Digite a coordenada Y do canto inferior esquerdo: ")
canto1 = Ponto(x1, y1)
x2 = input("digite a coodernada X do canto superior direito: ")
y2 = input("Digite a coordenada Y do canto superior direito: ")
canto2 = Ponto(x2, y2)
ret = Retangulo(canto1, canto2)
print (canto1, canto2)
print("Ponto central é %s" % repr(ret.centro()))