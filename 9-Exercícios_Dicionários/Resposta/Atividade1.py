cadastro = {}
while True:
    aluno = []
    notas = []
    media = 0
    nome = input('Nome do aluno: ')
    for n in range(0,3):
        while True:
            nota = float(input(f'Nota {n+1}: '))
            if 0<=nota<=10:
                break
        media += nota    
        notas.append(nota)
    aluno.append(notas)
    media = media/3
    aluno.append(media)
    cadastro[nome] = aluno
    print(cadastro)

    resposta = input('Deseja parar? [S]').upper()[0]

    if resposta != 'S':
        break

for chave, valor in cadastro.items():
    print('Alunos aprovados:')
    if valor[1] >= 7:
        print(f'  {chave}')

busca = input('Buscar aluno: ')
for chave, valor in cadastro.items():
    if chave == busca:
        if valor[1] >= 7:
            situacao = 'Aprovado'
        elif valor[1] >=4:
            situacao = 'Recuperação'
        else:
            situacao = 'Reprovado'
        print(f'Nome: {chave}\nMédia: {valor[1]}\nSituação: {situacao}')