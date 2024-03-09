vel = int(input('Insira a velocidade em KM: '))

# se a velocidade for maior que 80KM, multa. Senão, nada.
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado por excesso de velocidade. Valor da multa: R${:.2f}'.format(multa))
else:
    print('Dirija com cuidado e tenha um bom dia!')