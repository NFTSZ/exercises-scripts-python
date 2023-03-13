peso = float(input('Insira o seu peso: KG '))
altura = float(input('Insira a sua altura: '))

# calcula o imc dividindo o peso pela altura ao quadrado
imc = peso / (altura * altura)

print('Seu IMC é {:.2f}, você está'.format(imc))

# analisa e encaixa no status de acordo com o imc
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Com peso ideal')
elif 25 <= imc < 30:
    print('Em sobrepeso')
elif 30 <= imc < 40:
    print('Com obesidade')
else: 
    print('Com obesidade mórbida')
