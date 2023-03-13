dist =  int(input('Informe a distância da viagem em KM: '))

# vai calcular o preço de acordo com a distância em KM 
if dist <= 200:
    preco = 0.50 * dist
    print('O preço da sua viagem de distância {}Km é: R${:.2f}'.format(dist, preco))
else:
    preco = 0.45 * dist
    print('O preço da sua viagem de distância {}Km é: R${:.2f}'.format(dist, preco))
