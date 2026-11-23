senha_correta = "1234"
tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado")
        break
    tentativas += 1
    print("Senha incorreta")
if tentativas == 3:
    print("Acesso bloqueado")
