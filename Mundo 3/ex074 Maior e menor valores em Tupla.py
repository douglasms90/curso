# Crie um programa que vai gerar cinco n�meros aleat�rios e colocar em uma tupla.

#Depois disso, mostre a listagem de n�meros gerados e tambem indique o menor e o maior valor que est�o na tupla.






from random import randint

números = (randint(1,10), randint(1,10), randint(1,10), 
        randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')