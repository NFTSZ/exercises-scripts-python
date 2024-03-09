acumulador = 0
contador = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        contador += 1
        acumulador += impar
print('A soma de todos os {} valores é {}'.format(contador, acumulador))