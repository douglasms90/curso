# Refa�a o DESAFIO 035 dos tri�ngulos, acrescentando o recurso de mostrar que tipo de tri�ngulo ser� formado:

# Equil�tero: todos lados iguais
# Is�sceles: dois lados iguais
# Escaleno: todos os lados s�o diferentes




print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 == r2 and r2 == r3:
    print('O triângulo é Equilátero')
elif r1 == r2 or r2 == r3:
    print('Isósceles')
else:
    print('Escaleno')