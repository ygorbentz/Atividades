def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

lista = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29,
         32, 35, 38, 41, 44, 47, 50, 53, 56, 59]
n = ler_int("Digite o numero a buscar: ")
inicio = 0
fim = len(lista) - 1
pos = -1
while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == n:
        pos = meio
        break
    elif lista[meio] < n:
        inicio = meio + 1
    else:
        fim = meio - 1
if pos != -1:
    print("Encontrado no indice", pos)
else:
    print("Numero nao encontrado")
