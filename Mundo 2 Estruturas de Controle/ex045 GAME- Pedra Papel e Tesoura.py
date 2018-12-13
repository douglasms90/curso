# Crie um programa que fa�a o computador jogar jokenp� com voc�.

# Ex: pedra, papel, tesoura





from random import choice

jogada = str(input('Qual sua jogada? pedra, papel ou tesoura?'))
option = ['pedra', 'papel', 'tesoura']
computador = choice(option)

if jogada == 'pedra' and computador == 'tesoura':
    print('Eu joguei {} e o computador jogou {}, então eu ganhei'.format(jogada, computador))
elif jogada == 'papel' and computador == 'pedra':
    print('Eu joguei {} e o computador jogou {}, então eu ganhei'.format(jogada, computador))
elif jogada == 'tesoura' and computador == 'papel':
    print('Eu joguei {} e o computador jogou {}, então eu ganhei'.format(jogada, computador))
elif jogada == computador:
    print('Eu joguei {} e o computador jogou {}, então deu empate'.format(jogada, computador))
else:
    print('Eu joguei {} e o computador jogou {}, então o computador ganhou'.format(jogada, computador))