nota = float(input('Digite sua nota: '))

if nota < 5:
    print('Sua classificação é D')
elif 5 <= nota <= 6.9:
        print('Sua classificação é C')
elif 7 <= nota <= 8.9:
        print('Sua classificação é B')
else:
       print('Sua classificação é A')