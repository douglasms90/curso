# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.







aluno = ['', 0, 0]
cadastro = list()
while True:
    aluno[0] = str(input('Nome: '))
    aluno[1] = float(input('Nota 1: '))
    aluno[2] = float(input('Nota 2: '))
    cadastro.append(aluno[:])
    op = str(input('Quer continuar [S/N]: ')).lower().split()[0]
    if op == 'n':
        break
    else:
        pass

for alunos in range(0, len(cadastro)):
    print(f'{alunos + 1}º aluno: {cadastro[alunos][0]} média: {(cadastro[alunos][1] + cadastro[alunos][2]) / 2}')

while op != 999:
    op = int(input('Qual aluno gostaria de mais informação? '))
    print(f'{op}º aluno: {cadastro[op - 1][0]} primeira nota {cadastro[op - 1][1]}, segunda nota {cadastro[op - 1][2]}, média {(cadastro[op - 1][1] + cadastro[op - 1][2]) / 2}')
