def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

soma = 0
qtd = 0
nota = ler_float("Digite a nota (-1 para sair): ")
while nota != -1:
    if 0 <= nota <= 10:
        soma += nota
        qtd += 1
    else:
        print("Nota invalida")
    nota = ler_float("Digite a nota (-1 para sair): ")
if qtd > 0:
    print("Media:", round(soma / qtd, 2))
else:
    print("Nenhuma nota valida informada")
