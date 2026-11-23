def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

n = ler_int("Digite um numero inteiro nao negativo: ")
while n < 0:
    n = ler_int("Numero invalido. Digite novamente: ")
fat = 1
i = n
while i > 1:
    fat *= i
    i -= 1
print(n, "! =", fat)
