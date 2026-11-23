def ler_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite um numero valido")

notas = []
for i in range(10):
    notas.append(ler_float(f"Nota do aluno {i + 1}: "))
maior = notas[0]
menor = notas[0]
soma = 0
for n in notas:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Media da turma:", round(soma / 10, 2))
