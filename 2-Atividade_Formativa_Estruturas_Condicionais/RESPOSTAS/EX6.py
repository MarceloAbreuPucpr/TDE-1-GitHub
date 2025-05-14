valor = float(input('Digite o valor da compra: '))
valor_desconto = valor - (valor*0.1)

if valor > 100:
    print(f'O item de preço R${valor} obteve um desconto de 10% e ficou R${valor_desconto}')
else:
    print(f'O item não obteve desconto e se mantem R${valor}')