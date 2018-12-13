# Crie um programa que simule o funcionamento de um caixa eletr�nico. No in�cio, pergunte ao usu�rio qual ser� o valor a ser sacado (n�mero inteiro) e o programa vai informar quantas c�dulas de cada valor ser�o entregues.

# OBS: Considere que o caixa possui c�dulas de R$50, R$20, R$10 e R$1.





print('=' * 30) 
print('{:^30}'.format('BANCO CEV'))
print('=' * 30) 
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')