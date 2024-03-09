num = int(input('Digite um número inteiro: '))
primo = 0

for c in range(1, num + 1):
    if num % c == 0:
        primo += 1  
        
print('O número {} foi divisível {} vezes.'.format(num, primo))

if primo == 2:
    print('É considerado primo')
else:
    print('Não é considerado primo')