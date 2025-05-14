numero = int(input('Digite um número: '))
print(f'Tabuada do {numero}')

for multiplicador in range(0,11):
    print(f'{numero} x {multiplicador} = {numero*multiplicador}')