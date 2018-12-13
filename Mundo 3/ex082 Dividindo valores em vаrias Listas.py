# Crie um programa que vai ler v�rios n�meros e colocar em uma lista.

# Depois disso, crie duas listas extras que v�o conter apenas os valores pares e os valores impares digitados, repectivamente.

# Ao final, mostre o conte�do das tr�s listas geradas.




num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)        
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')