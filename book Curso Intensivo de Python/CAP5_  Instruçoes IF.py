carros = ['audi', 'bmw', 'subaru', 'toyota']
for carro in carros:        # o laço procura o valor indicado em IF
    if carro == 'bmw':
        print(carro.upper())    # ao encontrar o valor, o exibe com letras maiúsculas
    else:
        print(carro.title())

# teste condicional TRUE e FALSE 
>>> car = 'bmw'        # defina o valor da VAR como 'bmw'
>>> car == 'bmw'    # o valor de car é igual a 'bmw'?
True
>>> car == 'toyota'
False

# como python diferencia letras maiúsculas de minúsculas, no teste, poderá converter esse valor para letras minúsculas
>>> car = 'Audi'
>>> car.lower() == 'audi'
True

# == é usado para verificar igualdade e != para verificar diferença.

        # AND e OR
 # em AND, se um dos testes falhar, será avaliada como FALSE. 
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21    # se um E o outro é menor ou igual á 21
False

 >>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
 # em OR, será avaliada como FALSE apenas se ambos os testes falharem.
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21  # se um OU outro é menor ou igual á 21
True

>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False

 # IN e NOT IN
igredientes = ['frango', 'mussarela', 'calabresa', 'queijo', 'tomate']
if 'frango' in igredientes:
    print('O igrediente está na lista.')
# IN diz a python para verificar se o igrediente está na lista.

banidos = ['andrew', 'carolina', 'david']
usuario = 'marie'
if usuario not in banidos:
    print(usuario.title() + ", você pode postar o que quiser.")
# Se o valor de user não estiver na lista, Python devolverá True e executará a linha indentada
