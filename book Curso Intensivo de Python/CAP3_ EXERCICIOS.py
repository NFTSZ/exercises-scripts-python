''' Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir
uma mensagem para cada pessoa, convidando-a para jantar.'''

convidados = ['romulo', 'gilsao', 'izaq']
print('----------------------')
print ('Olá, voces foram convidados!')
print (convidados[0].title())
print (convidados[1].title())                   # TITLE() apresenta objetos com letra maiuscula no inicio
print (convidados[2].title())

'''Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não poderá
comparecer.'''
print('----------------------')
print ('o convidado', convidados[1].title(), 'não poderá comparecer :(')
print('----------------------')

''' Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando. Em seguida, utilize sua lista para exibir
uma mensagem para cada pessoa, convidando-a para jantar.'''

convidados = ['romulo', 'sabrina', 'izaq']
print ('Lista atualizada: espero vcs lá!')
print (convidados[0].title())
print (convidados[1].title())
print (convidados[2].title())
print('----------------------')

''' Acrescente uma instrução print no final de seu programa informando às pessoas que você 
encontrou uma mesa de jantar maior.'''
print('Boa! Conseguimos uma mesa maior, teremos mais convidados! :)')

''' Utilize insert() para adicionar um novo convidado no início de sua lista.'''
convidados.insert(0, 'milisa')
''' Utilize insert() para adicionar um novo convidado no meio de sua lista.'''
convidados.insert(3, 'robso')
'''Utilize append() para adicionar um novo convidado no fim de sua lista.'''
convidados.append('paula')
print('----------------------')
print (convidados[0].title())
print (convidados[1].title())
print (convidados[2].title())
print (convidados[3].title())
print (convidados[4].title())
print (convidados[5].title())
