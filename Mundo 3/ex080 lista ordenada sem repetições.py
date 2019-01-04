# Crie um programa onde o usu�rio possa digitar cinco valores num�ricos e cadastre-os em uma lista, j� na posi��o correta de inser��o 
# (sem usar o sort()).

# No final, mostre a lista ordenada na tela.

lista = []
for n in range(0,5):
    lista.append(int(input('Digite o número: ')))
print(f'A lista tem {lista}')
print(f'Em ordem fica {sorted(lista)}')