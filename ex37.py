alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
          "Fernanda", "Gabriel", "Helena", "Igor", "Julia"]
nome = input("Digite o nome: ").strip().lower()
achou = False
for a in alunos:
    if a.lower() == nome:
        achou = True
        break
if achou:
    print("Aluno cadastrado")
else:
    print("Aluno nao cadastrado")
