# Crie um programa que tenha uma tupla com v�rias palavras (n�o usar acentos). Depois disso, voc� deve mostrar, para cada palavra, quais s�o as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar'
            , 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')