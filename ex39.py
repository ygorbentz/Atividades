lista = [12, 45, 7, 89, 23, 56, 3, 91, 34, 67,
         15, 78, 42, 9, 61, 27, 84, 5, 39, 70]
maior = lista[0]
indice = 0
for i in range(1, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        indice = i
print("Maior valor:", maior)
print("Indice:", indice)
