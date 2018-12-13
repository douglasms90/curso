#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127 /n O número 6.127 tem a parte inteira 6.


#Com importação da biblioteca "math"




import math
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

# Com importação somente do "trunc" dentro da biblioteca "math"

from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

# Sem importação de biblioteca alguma

num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
