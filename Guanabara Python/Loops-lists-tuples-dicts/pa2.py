pt = int(input("insira o primeiro termo: "))
raz = int(input('Insira a razão: '))
termo = pt # c recebe o primeiro termo, pois o looping começa por ele
c = 1

while c <= 10: # enquanto o primeiro termo(c) for menor que o termo geral(termo)
    print('{} -> '.format(termo), end='')
    termo += raz  # primeiro termo + razao (menos(-) seria descrescente)
    c += 1
print('Fim')