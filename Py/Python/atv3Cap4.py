numeros=[]
i=0

while i <5:
    numeros.append(int(input("digite um número:")))
    i+=1
    maior=max(numeros)

print("O maior número é", maior)