def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

n = ler_int("Digite um numero inteiro positivo: ")
while n < 0:
    n = ler_int("Numero invalido. Digite um numero positivo: ")
while n >= 0:
    print(n)
    n -= 1
