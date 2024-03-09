num = int(input('Insira um número: '))
c = num # o fatorial smp começa no número. ex: 5! = 5 x 4, etc
f = 1   # fator nulo da multiplicação
print('{}! = '.format(num), end='')

# mostra os detalhes do fatorial enquanto c for maior que 0
while c > 0:
    # mostra o fatorial detalhado*
    print('{}'.format(c), end='')
    # se o 'c' for maior que 1 mostre 'x', senão mostre '='
    if c > 1:
        print(' x ' , end='')
    else:
        print(' = ', end='')
    # apenas isso calcula o fatorial
    f *= c
    c -= 1 
print('{}'.format(f)) # mostra o resultado final

num = int(input('Insira um número: '))
f = 1
print('{}! = '.format(num), end='')


# Mesmo código com FOR
'''for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
print(f)'''