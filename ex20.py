def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

base = ler_int("Base: ")
exp = ler_int("Expoente: ")
while exp < 0:
    exp = ler_int("Expoente invalido. Digite um valor nao negativo: ")
resultado = 1
for i in range(exp):
    resultado *= base
print(base, "^", exp, "=", resultado)
