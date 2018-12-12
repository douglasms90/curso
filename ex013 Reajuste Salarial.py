# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.








salário = float(input('Digite seu salário: R$'))
novo = salário + (salário * 15 / 100)
print('Seu salário era R${:.2f} e agora com aumento de 15% vale R${:.2f}:'.format(salário, novo))
