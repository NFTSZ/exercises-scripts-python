soma = 0
cont = 0
while True: # loop infinito
    num = int(input('Digite um número: [999 para parar] '))
    if num != 999:  # se o numero for diferente da flag
        soma += num  # some os numeros
        cont += 1
    else:
        break
print(f'Foram {cont} numeros digitados e a soma entre eles resulta em {soma}')
print('Fim do programa, volte sempre!')