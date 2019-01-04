# Fa�a um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador PERDER, mostrando o total de vit�rias consecutivas que ele conquistouno final do jogo.








from random import randint

print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 30)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end = '')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÌMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você VENCEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')