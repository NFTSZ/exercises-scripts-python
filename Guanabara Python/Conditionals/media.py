nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

# calcula a media das duas notas
media = (nota1 + nota2) / 2

print("Com a média {} você está: ".format(media))

# analisa a média e encaixa nos requisitos certos
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media <= 6.9:
    print('DE RECUPERAÇÃO')
else:
    print('APROVADO')