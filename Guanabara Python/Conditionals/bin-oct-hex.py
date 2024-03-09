num = int(input('Digite um número inteiro: '))
print('Escolha uma operação: \n[1] Binário\n[2] Octal\n[3] Hexadecimal')
opcao = int(input('> '))

# de acordo com a opçao escolhida, vai rodar a linha de código e tranformar em binario, octal ou hexadecimal

if opcao == 1:
    print('Seu número em BINÁRIO é: {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('Seu número em OCTAL é: {}'.format(oct(num)[2:]))
elif opcao == 3:
    print('Seu número em HEXADECIMAL é: {}'.format(hex(num)[2:]))
else:
    print('Opção INVÁLIDA.')