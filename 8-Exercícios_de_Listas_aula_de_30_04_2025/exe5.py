listaPar = []
listaImpar = []

for i in range(0, 5):
    numero = int(input(f'Digite o {i+1}° números: '))
    if numero%2==0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
        
if len(listaPar) == 0:
    print('Não foi digitado números pares')
else:
    print(f'O maior valor par é: {max(listaPar)}')

if len(listaImpar) == 0:
    print('Não foi digitado números impares')
else:
    print(f'O menor valor impar é: {min(listaImpar)}')