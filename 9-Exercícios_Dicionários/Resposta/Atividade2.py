Estoque = {}
while True:

    nome = input('Nome do produto: ')
    quantidade = int(input(f'Quantidade: '))

    Estoque[nome] = quantidade

    resposta = input('Deseja parar? [S]').upper()[0]

    if resposta != 'S':
        break

busca = input('Buscar produto: ')
print(Estoque.get(busca))

nome = input('Atualizar produto[nome]: ')
quantidade = int(input('Quantidade: '))
Estoque[nome] = quantidade
print(Estoque)