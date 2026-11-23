import random

def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um numero inteiro valido")

secreto = random.randint(1, 20)
while True:
    palpite = ler_int("Adivinhe o numero (1 a 20): ")
    if palpite > secreto:
        print("O numero secreto e menor")
    elif palpite < secreto:
        print("O numero secreto e maior")
    else:
        print("Acertou!")
        break
