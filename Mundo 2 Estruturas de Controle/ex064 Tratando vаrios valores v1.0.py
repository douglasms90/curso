# Crie um programa que leia v�rios n�meros inteiro pelo teclado. O programa vai parar quando o usu�rio digitar o valor 999, que � a condi��o de parada. No final, mostre quantos n�meros foram digitados e qual foi a soma entre eles (desconsiderando o flag).








num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))