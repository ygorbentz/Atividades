def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

lista = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29,
         32, 35, 38, 41, 44, 47, 50, 53, 56, 59]
n = ler_int("Digite o numero a buscar: ")

comp_linear = 0
pos_linear = -1
for i in range(len(lista)):
    comp_linear += 1
    if lista[i] == n:
        pos_linear = i
        break

comp_binaria = 0
pos_binaria = -1
inicio = 0
fim = len(lista) - 1
while inicio <= fim:
    meio = (inicio + fim) // 2
    comp_binaria += 1
    if lista[meio] == n:
        pos_binaria = meio
        break
    elif lista[meio] < n:
        inicio = meio + 1
    else:
        fim = meio - 1

print("Busca linear: indice", pos_linear, "-", comp_linear, "comparacoes")
print("Busca binaria: indice", pos_binaria, "-", comp_binaria, "comparacoes")
