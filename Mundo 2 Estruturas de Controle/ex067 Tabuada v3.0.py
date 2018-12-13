# Fa�a um programa que fa�a a tabuada de v�rios n�meros, um de cada vez, para cada valor para cada valor digitado pelo usu�rio. O programa ser� interrompido quando o n�mero solicitado for negativo.









while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')