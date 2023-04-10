alunos = {}  


for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota  

soma_notas = 0  


for nota in alunos.values():
    soma_notas += nota 

media = soma_notas / len(alunos)  

print("O dicionário de notas é:", alunos)
print("A média das notas é:", media)