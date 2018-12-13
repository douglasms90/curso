# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de coloca��o. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os �ltimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfab�tica.
# D) Em que posi��o da tabela est� o time da Chapecoense.



times = ('Atlético-MG', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 
       'América-MG ', 'São Paulo', 'Grêmio ', 'Vasco', 'Internacional ', 
       'Botafogo', 'Sport', 'Cruzeiro', 'Vitória', 'Santos', 'Chapecoense', 
       'Atlético-PR', 'Bahia', 'Ceará', 'Paraná')

print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[:5]}.')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')