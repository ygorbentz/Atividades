lista = [12, 11, 13, 5, 6, 7, 1, 9]
print("Lista inicial:", lista)
for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave
    print(f"Apos inserir {chave}:", lista)
print("Lista ordenada:", lista)
