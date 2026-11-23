def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

numeros = []
for i in range(20):
    numeros.append(ler_int(f"Digite o {i + 1}o numero: "))

def ordenar(lista):
    l = lista[:]
    n = len(l)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

while True:
    print("1 - Media")
    print("2 - Maior e menor")
    print("3 - Ordem crescente")
    print("4 - Ordem decrescente")
    print("5 - Busca linear")
    print("6 - Busca binaria")
    print("0 - Sair")
    op = input("Opcao: ")

    if op == "1":
        soma = 0
        for n in numeros:
            soma += n
        print("Media:", round(soma / len(numeros), 2))

    elif op == "2":
        maior = numeros[0]
        menor = numeros[0]
        for n in numeros:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        print("Maior:", maior)
        print("Menor:", menor)

    elif op == "3":
        print("Crescente:", ordenar(numeros))

    elif op == "4":
        cres = ordenar(numeros)
        dec = []
        for i in range(len(cres) - 1, -1, -1):
            dec.append(cres[i])
        print("Decrescente:", dec)

    elif op == "5":
        alvo = ler_int("Numero a buscar: ")
        comp = 0
        pos = -1
        for i in range(len(numeros)):
            comp += 1
            if numeros[i] == alvo:
                pos = i
                break
        if pos != -1:
            print("Encontrado no indice", pos)
        else:
            print("Nao encontrado")
        print("Comparacoes:", comp)

    elif op == "6":
        alvo = ler_int("Numero a buscar: ")
        lista = ordenar(numeros)
        comp = 0
        pos = -1
        inicio = 0
        fim = len(lista) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            comp += 1
            if lista[meio] == alvo:
                pos = meio
                break
            elif lista[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        print("Lista ordenada:", lista)
        if pos != -1:
            print("Encontrado no indice", pos, "da lista ordenada")
        else:
            print("Nao encontrado")
        print("Comparacoes:", comp)

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
