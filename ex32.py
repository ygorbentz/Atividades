def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

soma = 0
for i in range(10):
    n = ler_int(f"Digite o {i + 1}o numero: ")
    if n < 0:
        continue
    soma += n
print("Soma dos nao negativos:", soma)
