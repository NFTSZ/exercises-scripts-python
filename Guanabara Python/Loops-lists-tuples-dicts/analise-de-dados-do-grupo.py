cont = 0
mais18 = 0
masc = 0
mulhermenos20 = 0
while True:
    cont += 1
    print(f'======= Cadastro da {cont}° pessoa ==========')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').lower()
    querounao = int(input(' Deseja continuar?\n [1] Sim  [2] Não\n>>> '))
    if idade >= 18:
        mais18 += 1
    if sexo == 'm':
        masc += 1
    if sexo == 'f' and idade <= 20:
        mulhermenos20 += 1
    if querounao == 2:
        break
print(f'{mais18} com mais de 18 anos\n{masc} homens\n{mulhermenos20} mulheres com menos de 20 anos')
