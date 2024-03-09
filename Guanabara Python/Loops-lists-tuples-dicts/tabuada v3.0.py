from time import sleep
while True: 
    num = int((input('digite um numero inteiro: ')))    
    multi = 1   
    print('-=' *7)
    if num >= 0: 
        while multi <= 10:
            print('{} x {} = {}'.format(num, multi, multi * num))
            sleep(0.3)
            multi += 1  # o numero vai ser multiplicado pelo contador
    else:
        print('Apenas números inteiros. Execute novamente.')
        break
    print('-=' *7)
print('Fim do programa, volte sempre!')

'''o primeiro looping vai sempre dar input para o usuario inserir um numero inteiro.
    Se o número for positivo, ou seja, maior que zero, o programa irá exibir a tabuada 
    com um sleep de 0,2 segundos (visualmente bonito). Caso o número seja negativo, o 
    looping encerra mostrando a mensagem de finalização do programa.'''