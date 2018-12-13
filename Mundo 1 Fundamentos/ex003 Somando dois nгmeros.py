# Crie um programa que leia dois números e mostre a soma entre eles.








n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
s = n1 + n2
print('A soma entre', n1, 'e', n2, 'é', s,'!')

# Caso NÃO use a variável "s" futuramente no código, faça da seguinte forma

n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
print('A soma entre {} e {} é {}!'.format(n1, n2, (n1+n2)))
