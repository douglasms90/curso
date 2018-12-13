# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.








n = int(input('Digite um número:'))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {}, e seu sucessor é {}'.format(n, a, s))

# Caso NÃO use mais a variável "a" e "s" futuramente no código, faça da seguinte forma

n = int(input('Digite um número:'))
print('Analisando o valor {}, seu antecessor é {}, e seu sucessor é {}'.format(n, (n-1), (n+1)))
