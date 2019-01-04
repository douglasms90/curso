# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero at� vinte.

# Seu programa dever� ler um n�mero pelo teclado (entre 0 e 20) e mostr�-lo por extenso.






cont = ('zero', 'um', 'dois', 'tres', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove', 
       'dez', 'onze', 'doze', 'treze', 'quatorze', 
       'quinze', 'dezesseis', 'dezessete', 'dezoito', 
       'dezenove', 'vinte')
while True:
    num = int(input('Qual o número: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')