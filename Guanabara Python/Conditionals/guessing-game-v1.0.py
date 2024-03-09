from random import choice
from time import sleep

# seleciona um número aleatoriamente entre 0 e 5
num_computer = int(choice([0, 1, 2, 3, 4, 5]))

print('-=' *20)
print('O computador escolheu um número de 0 a 5')
print('-=' *20)

# entrada para o usuario inserir o seu palpite
num_player = int(input('Insira o seu palpite> '))

# pra ficar bonitinho
print('Processando...')
sleep(2)

# analisa se o palpite do usuario bate com o numero escolhido aleatoriamente
if num_player == num_computer:
    print('Parabéns, você acertou!')
else:
    print('Está errado.. tente novamente!')

print('O número escolhido foi {}'.format(num_computer))
