# Crie um programa que leia v�rios n�meros inteiros pelo teclado. O exercicio s� ir� parar quando o usu�rio digitar o valor 999, que � a condi��o de parada. No final, e mostre quantos n�meros foram digitados e qual foi a soma entre eles (desconsiderando o flag)








soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores é {soma}')