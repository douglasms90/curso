# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.








n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

# Caso NÃO use mais a variável "d, t, r" futuramente no código, faça da seguinte forma

n = int(input('Digite um número:'))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

# OU no lugar de "(n**(1/2))" colocar "pow(n, (1/2))"

print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))

# EXEMPLOS DE "{}"
#{:<20}  "            Douglas"
#{:>20}  "Douglas            "
#{:^20}  "      Douglas      "
#{:=^20} "======Douglas======"
#{:.2f}  "1.33"

# QUEBRA DE LINHA "\n"