alunos = []
while True:
    nome = input("Nome do aluno: ")
    alunos.append(nome)
    resp = input("Deseja continuar? (s/n): ").lower()
    if resp != "s":
        break
print("Alunos cadastrados:")
for a in alunos:
    print(a)
