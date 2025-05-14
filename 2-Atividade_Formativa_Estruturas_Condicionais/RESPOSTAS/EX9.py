salario = float(input('Digite seu salário: '))

if salario <= 20000:
    print('A alíquota de impostos é 0%')
elif 20000<salario<=50000:
    print('A alíquota de impostos é 15%')
else:
    print('A alíquota de impostos é 25%')