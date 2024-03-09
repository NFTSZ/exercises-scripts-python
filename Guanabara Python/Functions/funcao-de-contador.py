'''Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:    
a) de 1 até 10, de 1 em 1                      
b) de 10 até 0, de 2 em 2                     
c) uma contagem personalizada'''
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} a {f} pulando de {p}')
    print('-='*10)
    
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
        print('FIM')
    else:
        cont = i 
        while cont >= f:
            print(cont, end=' ')
            cont -= p
        print('FIM')
    print('-='*10)
    
        
contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a contagem: ')
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)