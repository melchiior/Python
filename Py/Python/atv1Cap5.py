n = []
while True:
    valor = int(input('digite a nota: '))
    if (valor == -1):
        break
    else: 
        n.append(valor)

media = (sum(n)/len(n))    

print(n)
print(len(n))
list.reverse(n)
print(n)

print(sum(n))
print(sum(n)/len(n))

media = (sum(n)/len(n)) 
for i in n:
    if i > media:
        print(i)

for x in n:
    if x < 7:
        print("valores menores que 7: \n",x)

print ('fim')