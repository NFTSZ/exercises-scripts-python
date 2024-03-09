frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for contrario in junto:
    inverso = junto[::-1]

print('A frase "{}" ao contrário é "{}"'.format(junto, inverso))

if junto == inverso:
    print('Esta frase É um palíndromo.')
else:
    print('Esta frase NÃO É um palíndromo.')