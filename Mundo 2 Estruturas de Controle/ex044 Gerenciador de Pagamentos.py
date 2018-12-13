# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu pre�o normal e condi��o de pagamento:

# � vista dinheiro / cheque: 10% de desconto
# � vista no cart�o: 5% de desconto
# Em at� 2x no cart�o: pre�o normal
# 3x ou mais no cart�o: 20% de juros



valor = float(input('Qual o valor do produto? R$'))

print('1 Àvista dinheiro / cheque.')
print('2 Àvista no cartão.')
print('3 Em até 2x no cartão.')
print('4 Em 3x ou mais no cartão')

forma = int(input('Qual a forma de pagamento? '))

if forma == 1:
    print('O valor é R${} e pagando no dinheiro / cheque será R${:.2f} com 10% de desconto.'.format(valor, ((valor - (valor * 10) / 100))))
elif forma == 2:
    print('O valor é R${} e pagando àvista no cartão será R${:.2f}'.format(valor, valor - (valor * 5) / 100))
elif forma == 3:
    print('O valor é R${} e pagando em 2x no cartão será R${:.2f}'.format(valor, valor))
else:
    print('O valor é R${} e pagando em 3x ou mais no cartão será R${:.2f}'.format(valor, valor + ((valor * 20) / 100)))