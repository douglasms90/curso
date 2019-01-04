# Fa�a um programa que leia dois n�meros inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor � maior
# O segundo valor � maior
# N�o existe valor maior, os dois s�o iguais




n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior.')
if n1 < n2:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS.')