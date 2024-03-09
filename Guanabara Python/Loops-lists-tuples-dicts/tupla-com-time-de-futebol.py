'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('América-MG', 'Atlético-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Chapecoense', 'Cruzeiro',
         'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacionl', 'Palmeiras', 'Bragantino',
         'Santos', 'São Paulo', 'Vasco da Gama')
print('--------------------------')
print(f'Lista de times: {times}')
print('--------------------------')
print(f'Os 5 primeiros times são: {times[0:5]}')
print('--------------------------')
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('--------------------------')
print('O Chapecoense está na {}º posição.'.format(times.index('Chapecoense')+1))
print('--------------------------')
print(f'Times em ordem alfabética: \n{sorted(times)}')
print('--------------------------')