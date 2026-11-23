def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

maior = None
n = ler_int("Digite um numero (0 para sair): ")
while n != 0:
    if maior is None or n > maior:
        maior = n
    n = ler_int("Digite um numero (0 para sair): ")
if maior is None:
    print("Nenhum numero informado")
else:
    print("Maior numero:", maior)
