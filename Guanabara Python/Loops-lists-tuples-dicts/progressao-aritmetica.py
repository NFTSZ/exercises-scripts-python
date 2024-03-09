pt = int(input("insira o primeiro termo: "))
raz = int(input('Insira a razão: '))

termo_geral = pt + (11-1) * raz

for c in range(pt, termo_geral, raz):
    print(c, end=' -> ')

print('Fim')