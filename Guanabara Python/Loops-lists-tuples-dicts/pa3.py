pt = int(input("insira o primeiro termo: "))
raz = int(input('Insira a razão: '))
termo = pt # c recebe o primeiro termo, pois o looping começa por ele
c = 1
seg = 10
mais = 0

while seg != 0:
    while c <= seg: # enquanto o primeiro termo(c) for menor que o termo geral
        print('{} -> '.format(termo), end='')
        termo += raz  # primeiro termo + razao (menos(-) seria descrescente)
        c += 1
    print('pausa')
    mais = int(input('Quantos termos mostrar a mais? '))
    seg += mais
    if mais == 0:
        break
print('Fim do programa, volte sempre!')
 