def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

nomes = []
medias = []
notas_alunos = []

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("0 - Sair")
    op = input("Opcao: ")

    if op == "1":
        nome = input("Nome: ")
        qtd = ler_int("Quantas notas? ")
        notas = []
        for i in range(qtd):
            nota = ler_float(f"Nota {i + 1}: ")
            while nota < 0 or nota > 10:
                nota = ler_float("Nota invalida. Digite de 0 a 10: ")
            notas.append(nota)
        soma = 0
        for n in notas:
            soma += n
        media = soma / qtd if qtd > 0 else 0
        nomes.append(nome)
        notas_alunos.append(notas)
        medias.append(media)
        print("Aluno cadastrado")

    elif op == "2":
        if len(nomes) == 0:
            print("Nenhum aluno cadastrado")
        for i in range(len(nomes)):
            print(nomes[i], "- Notas:", notas_alunos[i], "- Media:", round(medias[i], 2))

    elif op == "3":
        busca = input("Nome para pesquisar: ").strip().lower()
        pos = -1
        for i in range(len(nomes)):
            if nomes[i].lower() == busca:
                pos = i
                break
        if pos != -1:
            print(nomes[pos], "- Notas:", notas_alunos[pos], "- Media:", round(medias[pos], 2))
        else:
            print("Aluno nao encontrado")

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
