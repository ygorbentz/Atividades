palavra = input("Digite uma palavra: ").lower()
vogais = 0
for letra in palavra:
    if letra in "aeiouáéíóúâêôãõà":
        vogais += 1
print("Quantidade de vogais:", vogais)
