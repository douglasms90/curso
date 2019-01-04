# Fa�a um programa que calcule a soma entre todos os n�meros impares que s�o multiplos de tr�s e que se encontram no intervalo de 1 at� 500.







soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        soma += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
