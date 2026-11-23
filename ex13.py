def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

while True:
    n = ler_int("Digite um numero inteiro positivo: ")
    if n > 0:
        break
    print("Valor invalido")
print("Numero informado:", n)
