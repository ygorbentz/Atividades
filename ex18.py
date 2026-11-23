def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

soma = 0
for i in range(10):
    soma += ler_int(f"Digite o {i + 1}o numero: ")
print("Soma:", soma)
