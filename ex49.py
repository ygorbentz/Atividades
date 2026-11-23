def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

produtos = []
quantidades = []

while True:
    print("1 - Cadastrar produto")
    print("2 - Registrar quantidade")
    print("3 - Buscar produto")
    print("4 - Listar em ordem alfabetica")
    print("0 - Sair")
    op = input("Opcao: ")

    if op == "1":
        nome = input("Nome do produto: ").strip()
        if nome == "":
            print("Nome invalido")
            continue
        existe = False
        for p in produtos:
            if p.lower() == nome.lower():
                existe = True
                break
        if existe:
            print("Produto ja cadastrado")
            continue
        qtd = ler_int("Quantidade: ")
        if qtd < 0:
            print("Quantidade invalida")
            continue
        produtos.append(nome)
        quantidades.append(qtd)
        print("Produto cadastrado")

    elif op == "2":
        nome = input("Nome do produto: ").strip().lower()
        pos = -1
        for i in range(len(produtos)):
            if produtos[i].lower() == nome:
                pos = i
                break
        if pos == -1:
            print("Produto nao encontrado")
            continue
        qtd = ler_int("Nova quantidade: ")
        if qtd < 0:
            print("Quantidade invalida")
            continue
        quantidades[pos] = qtd
        print("Quantidade atualizada")

    elif op == "3":
        nome = input("Nome do produto: ").strip().lower()
        pos = -1
        for i in range(len(produtos)):
            if produtos[i].lower() == nome:
                pos = i
                break
        if pos != -1:
            print(produtos[pos], "- Quantidade:", quantidades[pos])
        else:
            print("Produto nao encontrado")

    elif op == "4":
        if len(produtos) == 0:
            print("Nenhum produto cadastrado")
            continue
        p = produtos[:]
        q = quantidades[:]
        n = len(p)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if p[j].lower() > p[j + 1].lower():
                    p[j], p[j + 1] = p[j + 1], p[j]
                    q[j], q[j + 1] = q[j + 1], q[j]
        for i in range(n):
            print(p[i], "- Quantidade:", q[i])

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
