lista = [64, 34, 25, 12, 22, 11, 90, 5, 47, 3]
n = len(lista)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print("Lista ordenada:", lista)
