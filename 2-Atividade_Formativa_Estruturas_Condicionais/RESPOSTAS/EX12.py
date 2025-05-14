peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Sua classificação é D')
elif 18.5 <= imc <= 25:
        print('Sua classificação é C')
elif 25 <= imc <= 30:
        print('Sua classificação é B')
else:
       print('Sua classificação é A')