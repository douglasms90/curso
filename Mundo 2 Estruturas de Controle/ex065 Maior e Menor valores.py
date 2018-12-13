# Crie um programa que leia v�rios n�meros inteiros pelo teclado. No final da execu��o, mostre a m�dia entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usu�rio se ele quer ou n�o continuar a digitar valores.







resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))