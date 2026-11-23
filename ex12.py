def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

while True:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("0 - Sair")
    op = input("Opcao: ")
    if op == "0":
        print("Saindo...")
        break
    if op not in ("1", "2", "3"):
        print("Opcao invalida")
        continue
    a = ler_float("Primeiro numero: ")
    b = ler_float("Segundo numero: ")
    if op == "1":
        print("Resultado:", a + b)
    elif op == "2":
        print("Resultado:", a - b)
    else:
        print("Resultado:", a * b)
