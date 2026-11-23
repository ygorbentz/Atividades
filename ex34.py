def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

soma = 0
qtd = 0
for i in range(10):
    nota = ler_float(f"Nota {i + 1}: ")
    if nota < 0 or nota > 10:
        continue
    soma += nota
    qtd += 1
if qtd > 0:
    print("Media:", round(soma / qtd, 2))
else:
    print("Nenhuma nota valida")
