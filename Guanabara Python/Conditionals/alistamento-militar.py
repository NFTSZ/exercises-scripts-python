from datetime import date

ano_atual = date.today().year

ano_nasc = int(input('Insira seu ano de nascimento: '))
idade = ano_atual - ano_nasc

if idade < 18:
    print('Vocẽ ainda não tem idade para se alistar. Volte daqui {} ano(s).'.format(18-idade))
elif idade == 18:
    print('Vocẽ já tem idade para se alistar.')
else:
    print('Voce devia ter se alistado há {} ano(s).'.format(idade-18))