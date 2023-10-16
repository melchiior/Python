perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
qtnsim = 0

for i in perguntas:
    res=input(i)
    if res in ("S", "s"):
        qtnsim += 1

if qtnsim < 2:
    print("\n Inocente \n")
elif qtnsim ==2:
    print("\n Suspeita \n")
elif qtnsim in (3,4):
    print("\n Cúmplice \n")
elif qtnsim == 5:
    print("\n Assassino \n")
    
