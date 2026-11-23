lista = [29, 10, 14, 37, 13, 5, 88, 1, 42, 21]
n = len(lista)
for i in range(n - 1):
    menor = i
    for j in range(i + 1, n):
        if lista[j] < lista[menor]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]
print("Lista ordenada:", lista)
