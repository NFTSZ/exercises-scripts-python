# laço FOR para executar  amesma ação em todos os itens da lista

nomes = ['julia', 'andré', 'paula', 'marcos']
for nome in nomes:          # "para todo NOME na lista de NOMES, exiba cada um"
    print('Olá', nome.title())
    print('Seja bem vindo(a)!\n')

print("Obrigado á todos por participarem.")

# trabalhando com numeros

for values in range(5):          # RANGE() serve para fazer contar até tal numero
    print(values)        # adicionando +1 ao VALUE, o RANGE() contará até 5
    
numeros = list(range(5))        # RANGE() dentro de LIST() faz com que os numeros sejam adicionados em uma lista
print(numeros)                 # nesse caso n funciona a dica do '+1', eu acho

pula_numero = list(range(1,10,2))        # lê-se 'de 1 ao 10 pulando 2 numeros'
print(pula_numero)

squares = []                              #   squares = []                      
for valores in range(1,11):               #   for valores in range(1,11):         de forma mais simples 
    square = valores**2                   #      squares.append(valores**2)     < adiciona diretamente á lista
    squares.append(square)                #   print(squares)
print(squares)
print(max(squares))     # maior numero da lista
print(min(squares))     # menor numero
print(sum(squares))     # soma de todos os numeros

# list comprehension permite gerar essa mesma lista com apenas uma linha de código.

quadrados = [value**2 for value in range(1,11)]
print(quadrados)


        # fatiando uma lista
    
jogadores = ['mariana', 'marcos', 'paulina', 'bruna', 'ricardo', 'fernanda']

print(jogadores[0:3])           # o codigo exibe os nomes no indice 0, 1 e 2
print(jogadores[:2])            # sem um indice inicial, ele retorna o inicio da lista
print(jogadores[4:])            # sem um indice final, ele retorna do numero que vc pediu até o fim da lista
print(jogadores[-3:])           # com indice negativo ele vai retornar uma determinada distância do final da lista

        # Percorrendo umafatia com o laço FOR
    
jogadores = ['mariana', 'marcos', 'paulina', 'bruna', 'ricardo', 'fernanda']
print("Aqui estão os três primeiros do time:")
                                  # Em vez de percorrer a lista inteira, percorre somente os três primeiros nomes
for jogador in jogadores[:3]:      
    print(jogador.title())
    
            # copiando uma lista
        
comida_fav = ['banana', 'pizza', 'sorvete']
fav_amigo = comida_fav[:]      # copia a lista da variavel anterior
comida_fav.append('uva')
fav_amigo.append('maçã')
print(comida_fav)           # mostrando q são listas diferentes
print(fav_amigo)


               # TUPLAS            usadas para armazenar um conjunto de valores que não devem ser modificados
    
dimensao = (30, 250)        #   TUPLAS usam parênteses e são imutáveis
print(dimensao)

for dimensoes in dimensao:  # é possível usar o laço FOR em uma TUPLA assim como em uma LISTA
    print(dimensoes) 

dimensao = (52, 125)
for dimensoes in dimensao:  # apesar de não ser possível alterar um valor espscífico da tupla, podemos alterá-la ao todo
    print(dimensoes)
