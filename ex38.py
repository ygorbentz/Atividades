def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

lista = [10, 25, 3, 47, 18, 6, 33, 50, 2, 14]
valor = ler_int("Digite um valor: ")
pos = -1
for i in range(len(lista)):
    if lista[i] == valor:
        pos = i
        break
if pos != -1:
    print("Encontrado no indice", pos)
else:
    print("Valor nao encontrado")
