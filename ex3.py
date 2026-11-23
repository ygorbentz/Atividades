def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

soma = 0
n = ler_int("Digite um numero (0 para sair): ")
while n != 0:
    soma += n
    n = ler_int("Digite um numero (0 para sair): ")
print("Soma:", soma)
