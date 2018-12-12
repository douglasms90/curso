# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras miaúsculas.
# O nome de todas minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome




nome = str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro tem {} letras'.format(nome.find(' ')))

# OU

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
