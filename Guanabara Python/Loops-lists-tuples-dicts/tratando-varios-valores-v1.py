num = int(input('Insira um valor: '))
c = 0
soma = num
parada = 999
while num != parada:
        num = int(input('Insira outro valor: '))
        c += 1
        if num != parada:
            soma += num
        else:
            break
print('Voce inseriu {} valores e a soma de todos eles é {}'.format(c, soma))
    