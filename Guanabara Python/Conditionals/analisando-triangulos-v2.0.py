lado1 = float(input('Insira a medida do primeiro lado: '))
lado2 = float(input('Insira a medida do segundo lado: '))
lado3 = float(input('Insira a medida do terceiro lado: '))

'''A condição dentro do if verifica se os lados são menores
 que a soma dos outros dois. Se essa condição 
 for verdadeira para todos os três pares de lados, então as 
 medidas inseridas formam um triângulo.'''

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('As medidas inseridas FORMAM um triângulo...')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO')
    else: 
        print('ISÓSCELES')
else:
    print('As medidas inseridas NÃO FORMAM um triângulo.')