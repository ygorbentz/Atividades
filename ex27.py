def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

estoque = ler_int("Quantidade inicial: ")
while estoque > 0:
    print("Estoque atual:", estoque)
    retirada = ler_int("Quantidade a retirar: ")
    if retirada <= 0:
        print("Quantidade invalida")
    elif retirada > estoque:
        print("Retirada maior que o estoque disponivel")
    else:
        estoque -= retirada
print("Estoque zerado")
