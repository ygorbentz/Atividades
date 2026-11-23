def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

idade = ler_int("Digite sua idade: ")
while idade < 0 or idade > 120:
    idade = ler_int("Idade invalida. Digite novamente: ")
print("Idade valida:", idade)
