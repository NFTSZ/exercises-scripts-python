v_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Agora informe o salário do comprador: R$'))
anos = int(input('Em quantos anos o imóvel será pago? '))

v_mensal = v_casa / (anos * 12)
porcentagem = 30/100 * salario

print('O valor mensal é de R${}'.format(v_mensal))

if v_mensal > porcentagem:
    print('O seu emprestimo NÃO PODE ser aprovado.')
else:
    print('Seu empréstimo foi aprovado!')
