# Refa�a o DESAFIO 009, mostrando a tabuada de um n�mero que o usu�rio escolher, s� que agora utilizando um la�o for.







num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} + {} = {}'.format(c, num, num+c))
print('')
for c in range(0, 9):
    print('{} - {} = {}'.format(c, num, num-c))
print('')
for c in range(0, 9):
    print('{} x {} = {}'.format(c, num, num*c))
print('')