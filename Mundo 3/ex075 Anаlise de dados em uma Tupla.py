# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posi��o foi digitado o primeiro valor 3.
# C) Quais foram os n�meros pares.




núm = (int(input('digite o primeiro número: ')),
       int(input('digite o segundo número: ')),
       int(input('digite o terceiro número: ')),
       int(input('digite o quarto número: ')))

print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')