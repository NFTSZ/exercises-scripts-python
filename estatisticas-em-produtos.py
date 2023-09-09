cont = 0
lista = []
maismil = 0
barato = ''

while True:
    cont += 1
    print(f'======= Cadastro do {cont}° produto ==========')
    nome = str(input('Nome: '))
    preco = float(input('Preço: R$ '))
    lista.append(preco)
    querounao = int(input(' Deseja continuar?\n [1] Sim  [2] Não\n>>> '))
    
    if preco >= 1000:
        maismil += 1
    if min(lista):
        barato = nome.title()
    if querounao == 2:
        break
print('-=' *20)
print(f'Total gasto: {sum(lista):.2f}\nProdutos acima de R$1000: {maismil}\nO produto mais barato: {barato}')


