def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

lista = [5, 12, 7, 3, 20, 15, 8, 1, 30, 9]
n = ler_int("Digite um numero: ")
achou = False
for x in lista:
    if x == n:
        achou = True
        break
if achou:
    print("O numero esta na lista")
else:
    print("O numero nao esta na lista")
