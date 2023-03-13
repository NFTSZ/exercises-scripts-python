s = str(input('Insira o sexo: [M/F] ')).lower().strip()

while s != 'm' and s != 'f':
   s = str(input('Opção inválida. Insira novamente: ')).lower()

if s == 'm':
   print('Agradecemos palos dados. Sexo MASCULINO registrado.')
elif s == 'f':
   print('Agradecemos palos dados. Sexo FEMININO registrado.')