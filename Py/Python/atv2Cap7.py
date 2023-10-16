import random


palavras = input("Digite as palavras: ")
palavras = palavras.split(" ")

uma_palavra = palavras[random.randrange(0,len(palavras))]
palavra_forca = ["_" for i in uma_palavra]
chance = 1
while (chance < 7 and palavra_forca.count("_") != 0):
    letra = input("Digite uma letra: ")
    if (letra in uma_palavra): 
        print("A palavra é: ", end=" ")
        for p in range(len(uma_palavra)):
            if letra == uma_palavra[p]:
                del palavra_forca[p]
                palavra_forca.insert(p,letra)
        print(" ".join(palavra_forca))
    else:
        print("-> Você errou pela " + str(chance) + "a vez. Tente de novo!")
        chance = chance + 1
    if palavra_forca.count("_") == 0:
        print("Parabéns! Você acertou a palavra.")
    else:
        print("Forca! Fim de jogo.")