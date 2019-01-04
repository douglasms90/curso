# Crie um programa onde o usu�rio possa digitar v�rios valores num�ricos e cadastre-os em uma lista. Caso o n�mero j� exista
# l� dentro, ele n�o ser� adicionado. No final, ser�o exibidos todos os valores �nicos digitados, em uma ordem crescente.







números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')