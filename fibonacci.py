n = int(input('Quantos termos quer mostrar? '))
primeiro_termo = 0
segundo_termo = 1   # a sequencia começa com 0 e 1

print('{} -> {}'.format(primeiro_termo, segundo_termo), end='')

contador = 3  #recebe 3 pois os 3 primeiros ja estao calculados

while contador <= n:
    terceiro_termo = primeiro_termo + segundo_termo  # o terceiro é o primeiro com o segundo
    print(' -> {}'.format(terceiro_termo), end='')
    '''pra fazer o looping de ultimo + penultimo com a
    sequencia certa: o primeiro se torna o segundo e o 
    segundo o terceiro para que o terceiro seja a soma dos dois
    anteriores. O contador recebe 1 para cada valor já calculado'''
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    terceiro_termo = primeiro_termo + segundo_termo
    contador += 1
print(' -> fim') 