def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

n = ler_int("Digite um numero: ")
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
