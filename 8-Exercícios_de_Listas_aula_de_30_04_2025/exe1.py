def exerci1(lista, numero = 0, txt = 'Digite um número: '):
    for i in range(0,numero):
        numero = int(input(txt))
        lista.append(numero)
    return lista