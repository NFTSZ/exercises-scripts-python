soma = 0
for c in range(6):
    c = int(input('Digite um número inteiro: '))
    if c % 2 == 0:
        soma += c
print('A soma dos números pares inseridos é', soma)
