salario = float(input('Digite seu salário em reais: '))
tempo = float(input('Digite o seu tempo de serviço em anos: '))

if tempo > 5:
    print(f'Seu salário atual é igual a R${salario+(salario*0.05):.2f}')
else:
    print(f'Seu salário atual é igual a {salario:.2f}')

