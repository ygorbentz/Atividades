v1 = v2 = v3 = 0
while True:
    voto = input("Vote 1, 2 ou 3 (0 para encerrar): ")
    if voto == "0":
        break
    if voto == "1":
        v1 += 1
    elif voto == "2":
        v2 += 1
    elif voto == "3":
        v3 += 1
    else:
        print("Voto invalido")
print("Opcao 1:", v1, "votos")
print("Opcao 2:", v2, "votos")
print("Opcao 3:", v3, "votos")
