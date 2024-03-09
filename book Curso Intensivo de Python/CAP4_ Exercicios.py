
'''Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço FOR para exibir o nome de cada
pizza.'''

pizzas = ['portuguesa', 'gula', 'toscana']

'''Modifique seu laço for para mostrar uma frase usando o nome da pizza em vezde exibir apenas o nome dela.
Para cada pizza, você deve ter uma linha na saída contendo uma frase simples como Gosto de pizza de pepperoni.
Acrescente uma linha no final de seu programa, fora do laço for, que informe quanto você gosta de pizza'''

for pizza in pizzas:
    print('Gosto da pizza', pizza.title())
print('\nGosto tanto que como todos os dias!\n\n')



'''Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes 
desses animais em uma lista e, então, utilize um laço FOR para exibir o nome de cada animal.'''

animais = ['gato', 'coelho', 'cachorro']

'''modifique seu programa para exibir uma frase sobre cada animal, por exemplo,
Um cachorro seria um ótimo animal de estimação. Acrescente uma linha no final de seu programa 
informando o que esses animais têm em comum.'''

for animal in animais:
    print('Um', animal, 'seria um ótimo pet')
print('\nTodos são fofos, inteligentes e amáveis.')


        # FOR  e RANGE()
'''– Contando até vinte: Use um laço for para exibir os números de 1 a 20,
incluindo-os.'''
for numeros in range(1,21):
    print(numeros)

    
'''– Um milhão: Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números.'''
lista = list(range(1,1000000))
for numero in lista:
    print(numero)

    
'''– Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min() e max()
para garantir que sua lista realmente começa em um e termina em um milhão. Além disso, utilize a 
função sum() para ver a rapidez com que Python é capaz de somar um milhão de números.'''
lista = list(range(1,1000000))
print(min(lista))
print(max(lista))
print(sum(lista))


'''– Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os
números.'''
num_impar = list(range(1,20,2))
for impares in num_impar:
    print(impares)

    
'''– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.'''
num_mult = list(range(3,30,3))
for multiplos in num_mult:
    print(multiplos)

    
'''– Cubos: Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10),
e utilize um laço for para exibir o valor de cada cubo.'''
dez_cubos = []
for cubos in range(1,10):
    dez_cubos.append(cubos**3)
print(dez_cubos)


'''– Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.'''
dez = [cubo**3 for cubo in range(1,10)]
print(dez)


# FATIAS 

'''Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia
para exibir os três primeiros itens da lista desse programa. Use uma fatia para exibir três
itens do meio da lista. Use uma fatia para exibir os três últimos itens da lista'''

exemplo1 = ['lapis', 'caneta', 'borracha', 'caderno', 'estojo']
print('Os três primerios itens da lista são:', exemplo1[:3])
print('Os três itens do meio da lista são:', exemplo1[1:4])
print('Os três últimos itens da lista são:', exemplo1[2:])


'''Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes'''

pizzas = ['portuguesa', 'gula', 'toscana']
friend_pizzas = pizzas[:]           # copia uma lista de uma variavel para outra variavel 
pizzas.append('calabresa')
friend_pizzas.append('siciliana')
print('minhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza)
print('\ne as do meu amigo são:')
for fpizza in friend_pizzas:
    print(fpizza)


'''– Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços
for para fazer exibições a fim de economizar espaço. Escolha uma versão de
foods.py e escreva dois laços for para exibir cada lista de comidas.'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for fr_food in friend_foods:
    print(fr_food)

    # TUPLAS
    
'''– Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos simples e
armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida,
use um laço for para exibir cada um dos itens do cardápio revisado.'''

pratos = ('filé', 'macarronada', 'frango à passarinho', 'feijoada', 'salada')
print('Pratos disponíveis:')
for prato in pratos:
    print(prato)

# pratos[2] = 'costela'   ERRO

pratos = ('filé', 'mac and cheese', 'frango grelhado', 'feijoada', 'salada')
print('Pratos disponíveis:')
for prato in pratos:
    print(prato)

