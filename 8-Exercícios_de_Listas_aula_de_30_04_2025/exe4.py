nota_alunos = []
numero=int(input('Quantidade de alunos: '))
reprovados = 0

for i in range(0, numero):
    nota = int(input(f'Digite a {i+1}° nota: '))
    nota_alunos.append(nota)
    if nota < 60:
        reprovados += 1

print(f'Número de reprovados = {reprovados}')
print(f'Número de aprovados = {numero-reprovados}')
