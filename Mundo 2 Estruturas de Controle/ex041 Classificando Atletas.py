# A confedera��o nacional de nata��o precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# At� 9 anos: MIRIM
# At� 14 anos: INFANTIL
# At� 18 anos: JUNIOR
# At� 20 anos: S�NIOR
# Acima: MASTER


from datetime import date

atual = date.today().year
nascimento = int(input('Quando você nasceu: '))
anos = atual - nascimento

if anos <= 9:
    print('MIRIM')
elif anos <= 14:
    print('INFANTIL')
elif anos <= 18:
    print('JUNIOR')
elif anos <= 20:
    print('SÊNIOR')
else:
    print('MASTER')