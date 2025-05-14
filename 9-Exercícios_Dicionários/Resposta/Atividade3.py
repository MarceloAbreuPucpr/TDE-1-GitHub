frase = input('Digite uma frase: ')
frase = frase.lower().replace(" ", "")  # Convertendo para minúsculas e removendo espaços
frequencia = {}

for letra in frase:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(f'Frequência das letras: {frequencia}')
