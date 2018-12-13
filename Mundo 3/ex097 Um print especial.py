# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre a mensagem com tamanho adaptável.

# Ex: escreva('Olá, Mundo!')

# Saída:
 # --------------------
 #      Olá, Mundo!
 # --------------------

def escreva(msg):
  tam = len(msg) + 4
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Pyton no Youtube')
escreva('CeV')