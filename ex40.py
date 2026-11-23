lista = [12, 45, 7, 89, 23, 56, 3, 91, 34, 67,
         15, 78, 42, 9, 61, 27, 84, 5, 39, 70]
menor = lista[0]
indice = 0
for i in range(1, len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        indice = i
print("Menor valor:", menor)
print("Indice:", indice)
