from exe1 import exerci1

a = []
exerci1(a, 10)

posicao = 1
for elemento in a:
    print(f'O {posicao}° número é: {elemento}')
    posicao += 1

print(f'O maior valor digitado foi {max(a)}')
print(f'O menor valor digitado foi {min(a)}')