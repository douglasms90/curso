# Fa�a um programa que leia o sexo de uma pessoa, mas s� aceite valores 'M' ou 'F'. Caso esteja errado pe�a a digita��o novamente at� ter um valor correto.






sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))