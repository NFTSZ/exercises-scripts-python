from datetime import datetime
from dateutil.relativedelta import relativedelta
 
dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(':'))

dia_final = int(input().split()[1])
hora_final, minuto_final, segundo_final = map(int, input().split(':'))

data1 = datetime(2024, 4, dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
data2 = datetime(2024, 4, dia_final, hora_final, minuto_final, segundo_final)

# funcao de lib externa q calcula e divide automaticamente a diferenca de duas datas 
diferenca = relativedelta(data2, data1)

print(f"{diferenca.days} dia(s)\n{diferenca.hours} hora(s)\n{diferenca.minutes} minuto(s)\n{diferenca.seconds} segundo(s)")

'''
# calculando, extraindo dias, horas, minutos e segundos de forma manual

duracao = data2- data1

# w = dias; x = horas; y = minutos; z = segundos  todos de duracao total
w = duracao.days
segundos_totais = duracao.seconds
x = segundos_totais // 3600
y = (segundos_totais % 3600) // 60
z = segundos_totais % 60

print(f'{w} dia(s)')
print(f'{x} hora(s)')
print(f'{y} minuto(s)')
print(f'{z} segundo(s)')
'''