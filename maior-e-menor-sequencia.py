lista = []
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    lista.append(peso)
print('O maior peso foi {}KG e o menor {}KG'.format(max(lista), min(lista)))