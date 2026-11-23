def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

saldo = 0
while True:
    print("Saldo:", saldo)
    print("1 - Depositar")
    print("2 - Sacar")
    print("0 - Sair")
    op = input("Opcao: ")
    if op == "1":
        valor = ler_float("Valor do deposito: ")
        if valor > 0:
            saldo += valor
        else:
            print("Valor invalido")
    elif op == "2":
        valor = ler_float("Valor do saque: ")
        if valor <= 0:
            print("Valor invalido")
        elif valor > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opcao invalida")
