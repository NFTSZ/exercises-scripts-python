salario = float(input('Insira o seu salário: R$'))

# o aumento de salários maiores de 1250 é de 10%, o aumento de salários menores é de 15%
if salario > 1250:
    aumento = 10 / 100 * salario
    total = aumento + salario
    print('Seu aumento é de {:.2f} reais. Salario atual: {:.2f}'.format(aumento, total))
else:
    aumento = 15 / 100 * salario
    total = aumento + salario
    print('Seu aumento é de {:.2f} reais. Salario atual: {:.2f}'.format(aumento, total))
