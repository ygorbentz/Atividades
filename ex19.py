def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

soma = 0
for i in range(5):
    soma += ler_float(f"Digite a nota {i + 1}: ")
media = soma / 5
print("Media:", round(media, 2))
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
