lista = []
nomevelho = ''
menos20 = 0

for n in range(1, 5):
    print('---- cadastro da {}° pessoa ----'.format(n))
    nome = str(input('Digite o nome: ')).strip().lower()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Insira o sexo [M/F]: ')).strip().lower()
    lista.append(idade)

    if sexo == 'm' and idade == max(lista):
        nomevelho = nome.title()
    if sexo == 'f' and idade < 20:
        menos20 += 1

media = (sum(lista)) / 4

print('---- Resultado ----')
print('A média de idade do grupo é {}'.format(media))
print('{} é o nome do homem mais velho.'.format(nomevelho))
print('há um total de {} mulheres com menos de 20 anos.'.format(menos20))