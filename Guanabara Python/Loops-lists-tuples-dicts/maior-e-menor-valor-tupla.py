'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na
tupla.'''
from random import randint

tupla = []
for i in range(0,5):
    num = randint(0, 10)
    tupla.append(num)

print(f'Números gerados: {tupla}')
print(f'Maior número: {max(tupla)}')
print(f'Menor número: {min(tupla)}')