#!/usr/bin/python
# -*- coding: utf-8 -*-

# Escreva um programa para aprovar o emprestimo banc�rio para a compra de uma casa.
# O programa vai perguntar o valor da casa, o sal�rio do comprador e em quantos anos ele vai pagar.

# Calcule o valor da presta��o mensal, sabendo que ele n�o pode exceder 30% do sal�rio ou ent�o o emprestimo ser� negado.


casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento> '))
prestação = casa / (anos * 12)
mínimo = (salário * 30) / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))

if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')