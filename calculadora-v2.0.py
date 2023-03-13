from time import sleep

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('-------------------------------------')
    print('''Selecione uma opção:
    [1] Somar
    [2] Multiplicar 
    [3] Maior número
    [4] Inserir novos números
    [5] Sair do programa''')

    opcao = int(input('>>> '))

    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {:.2f} e {:.2f} é {:.2f}'.format(num1, num2, soma))
        sleep(1)
    elif opcao == 2:
        multi = num1 * num2
        print('O produto entre {:.2f} e {:.2f} é {:.2f}'.format(num1, num2, multi))
        sleep(1)
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print('O maior é: {}'.format(maior))
            sleep(1)
        else:
            maior = num2
            print('O maior é: {}'.format(maior))
            sleep(1)
    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        sleep(1)
    elif opcao == 5:
        break
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa, Volte sempre.')