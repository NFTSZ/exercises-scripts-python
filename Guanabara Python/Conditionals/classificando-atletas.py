from datetime import date

# data o ano atual
ano_atual = date.today().year

# pede o ano de nascimento do usuário
ano_nasc = int(input('Insira seu ano de nascimento: '))

# descobre a idade do usuário de acordo com o ano inserido
idade = ano_atual - ano_nasc

print('-=-' * 15)
print('De acordo com sua idade: {} anos'.format(idade))
print('você é da categoria:')

# analisa e encaixa nos requisitos de idade
if idade <= 9:
    print('     MIRIM')
elif 10 <= idade <= 14:
    print('     INFANTIL')
elif 15 <= idade <= 19:
    print('     JÚNIOR')
elif 20 <= idade <= 25:
    print('     SÊNIOR')
else:
    print('     MASTER')
print('-=-' * 15)
