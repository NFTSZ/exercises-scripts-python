valores = int(input('Quantos valores deseja inserir? '))
lista = []  # lista vazia para armazenar os valores
c = 0   # contador de repetiçoes do loop

while valores != 0: # enquanto o input 'valores' for diferente de zero, libera o input 'valor'
    while c < valores:  # enquanto o contador for menor que a quantidade de valores requeridos: 
        valor = int(input('Insira um valor: '))   # peça um valor
        lista.append(valor) #adicione á lista
        c += 1  # confirme cada passager até ser igual ao 'valores' e encerrar o looping  
    media = sum(lista) / len(lista) # a média da lista é igual a soma de todos os numeros com a quantidade de elementos 
    print('A média dos valores é {}\nO maior valor foi {} e o menor {}'.format(media, max(lista), min(lista)))
    # codigo acima dando certo 
    
    # codigo abaixo dando aparentemente certo
    print('Deseja continuar digitando valores? [S/N] ')
    simnao = str(input('>>> ')).lower()
    
    if simnao == 's':  # se o usuario quiser inserir mais valores: 
        valores = int(input('Quantos valores deseja inserir? '))    
        c -= c  # zera o contador pra n dar conflito
        lista = []  # zera a lista pra n dar conflito
        while c < valores: # mesmo looping da primeira parte do código
            valor = int(input('Insira um valor: '))
            lista.append(valor)
            c += 1
    else:   # senão, encerra o looping
        break
print('Fim do programa, volte sempre!')