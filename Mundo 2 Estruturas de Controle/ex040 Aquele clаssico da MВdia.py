# Crie um programa que leia duas notas de um aluno e calcule sua m�dia, mostrando uma mensagem no final, de acordo com a m�dia atingida.

# M�dia abaixo de 5.0: REPROVADO

# M�dia entre 5.0 e 6.9: RECUPERA��O

# M�dia 7.0 ou superior: APROVADO


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

if média < 5.0:
    print('REPROVADO')
if média >= 7.0:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')