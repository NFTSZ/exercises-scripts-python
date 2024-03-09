'''– Testes condicionais: Escreva uma série de testes condicionais. Exiba uma frase que descreva o teste e 
o resultado previsto para cada um.
• Observe atentamente seus resultados e certifique-se de que compreende por que
cada linha é avaliada como True ou False.'''

carro = 'audi'
print('Esse carro == audi? Prevejo True.')
print(carro == 'audi')
print('\nEsse carro == bmw? Prevejo False.')
print(carro == 'bmw')

# TESTES CONDICIONAIS

'''Tenha pelo menos um resultado True e um False para cada um dos casos a seguir:'''
# • testes de igualdade e de não igualdade com strings;
string_1 = 'A'
string_2 = 'a'
print(string_1 == string_2)    # FALSE

string_1 = 'a'
string_2 = 'a'
print(string_1 == string_2)    # TRUE

# • testes usando a função lower();
carros = 'Audi'
print(carros.lower() == 'audi',    # TRUE
    carros.lower() == 'bmw'        # False
    )

# • testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a;
idade_1 = 28
idade_2 = 36
print(idade_1 == idade_2,                     # False
    idade_1 != idade_2, idade_1 < idade_2,    # True, True
    idade_1 > idade_2, idade_1 <= idade_2,    # False, True    
    idade_1 >= idade_2                        # False
    )       # organização de acordo com PEP 8
    
# • testes usando as palavras reservadas and e or;
numero_1 = 132
numero_2 = 9
print(numero_1 < 200 and numero_2 < 200,    # numero_1 menor que 200 e numero_2 menor que 200?      True
    numero_1 > 200 or numero_2 > 200        # numero_1 maior que 200 ou numero_2 maior que 200?     False
    )
    
# • testes para verificar se um item está em uma lista;
lista_carros = ['audi', 'bmw', 'subaru', 'ferrari']
for carro in lista_carros:
    if carro == 'audi':
        print('Possui.')         # Possui
        
# • testes para verificar se um item não está em uma lista.
carro_vendido = 'toyota'
if carro_vendido not in lista_carros:
    print('Não possui.')        # Não Possui.
