# Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um n�mero entre 0 a 10. S� que agora o jogador vai tentar advinhar at� acertar, mostrando no final quantos palpites foram necess�rios para vencer.








from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpites))