#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.



# OU sem importação de biblioteca alguma




co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

# Com importação de toda biblioteca "math"

import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

# Com importação somente do "trunc" dentro da biblioteca "math"

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hypotenusa vai medir: {:.2f}'.format(hi))
