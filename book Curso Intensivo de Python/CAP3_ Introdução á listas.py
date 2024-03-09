#lista
name = ['Romulo', 'Luana', 'Melissa', 'Manoel', 'Isaac']
print(name)

#substitui um item na lista
name[2] = 'Sabrina'
print(name)

# adiciona um item na lista
name.append("Melissa")
print(name)

# adiciona um item em um lugar especifico da lista
name.insert(4, "Gilsao")
print(name)

# deleta um item da lista se a posição for conhecida
del name[6]
print(name)

# A função POP() remove o item da lista mas ainda é permite usar o item se armazenado em outra variavel
popped_name = name.pop(5)
print(name)
print(popped_name)       # variavel em que o item removido foi armazenado

# a função POP() tbm serve para identificar o ultimo item armazenado na lista
last = name.pop()
print(last)
'''quando quiser apagar um item de uma lista e esse item não vai ser usado de modo algum, utilize a instrução DEL;
 se quiser usar um item depois que removê-lo, utilize o método POP().'''

# a função REMOVE() é usada quando n se sabe a posição o objeto
name.remove('Manoel')
print(name)



         # TODOS OS VALORES DA LISTA UTILIZAM LETRAS MINUSCULAS

# o metodo SORT() organiza a lista em ordem alfabética de forma PERMANTE
name = ['romulo', 'bruno', 'sofia', 'amanda']
name.sort()
print(name)

# ordem alfabética inversa, passando o argumento REVERSE=TRUE ao método SORT()
name = ['romulo', 'bruno', 'sofia', 'amanda']
name.sort(reverse=True)
print(name)

# o metodo SORTED() organiza a lista em ordem alfabética mas não de forma permanente
name = ['romulo', 'bruno', 'sofia', 'amanda']
print('ordem alfabetica: \n\t', sorted(name))   # \n é quebra de linha e \t é tubulação
print('lista original: \n\t', name)             # essa função também aceita reverse=True

# REVERSE() inverte a ordem da lista permanentemente mas dá para retomar ao original aplicando REVERSE() novamente
name = ['romulo', 'bruno', 'sofia', 'amanda']
name.reverse()
print(name)

# LEN() é usado para identificar a o tamanho de uma lista
name = ['romulo', 'bruno', 'sofia', 'amanda']
print(len(name))
