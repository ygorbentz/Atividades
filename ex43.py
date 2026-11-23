def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

numeros = []
for i in range(10):
    numeros.append(ler_int(f"Digite o {i + 1}o numero: "))
print("Ordem crescente:", sorted(numeros))
