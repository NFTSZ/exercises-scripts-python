from datetime import date

atual = date.today().year
maioridade = 0
menoridade = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimentoda {}° pessoa: '.format(c)))
    idade = atual - ano # variavel apenas dentro do laço pois n preciso dela fora
    if idade >= 21:
        maioridade += 1
    else: 
        menoridade += 1

print('{} pessoa(s) atingiram a maioridade\n{} pessoa(s) ainda não atingiram'.format(maioridade, menoridade))