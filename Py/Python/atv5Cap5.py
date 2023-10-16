c1 = 0
c2 = 0
c3 = 0
eleitores = int(input("Qual o numero de eleitores:"))
for i in range(eleitores):
    voto = input(
        "digite o número (1/2/3) do candidato em quem o "f"eleitor {i+1} quer votar:"
    )
    if voto == "1":
        c1 += 1
    if voto == "2":
        c2 += 2
    if voto == "3":
        c3 += 1


print(
    "Votação encerrada"
    f"\nCandidato 1: {c1} voto(s)"
    f"\nCandidato 2: {c2} voto(s)"
    f"\nCandidato 3: {c3} voto(s)"
)
