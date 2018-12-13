# Fa�a um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:

# Se ele vai se alistar ao servi�o militar.
# Se � a hora de se alistar
# Ou se j� passou do tempo de se alistamento

# Seu programa tambem ter� que mostrar o tempo que falta ou que passou do prazo.


from datetime import date

atual = date.today().year
nasc = int(input('Qual sua data de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você jé deveria ter se alista há {} anos'.format(saldo))
    ano  = atual - saldo
    print('Seu alistamento foi em {} ano'.format(anos))
