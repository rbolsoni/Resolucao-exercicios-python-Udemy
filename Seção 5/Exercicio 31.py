# Exercicio 31 - Classificação IMC

peso = float(input('Qual o seu peso em kg?'))
altura = float(input('Qual a sua altura em metros?'))

if peso < 60 and altura < 1.20:
    print('Sua classificação é A')
elif peso < 60 and 1.20 <= altura <= 1.70:
    print('Sua classificação é B')
elif peso < 60 and altura > 1.70:
    print('Sua classificação é C')
elif 60 <= peso < 90 and altura < 1.20:
    print('Sua classificação é D')
elif 60 <= peso < 90 and 1.20 <= altura <= 1.70:
    print('Sua classificação é E')
elif 60 <= peso < 90 and altura > 1.70:
    print('Sua classificação é F')
elif peso > 90 and altura < 1.20:
    print('Sua classificação é G')
elif peso > 90 and 1.20 <= altura <= 1.70:
    print('Sua classificação é H')
elif peso > 90 and altura > 1.70:
    print('Sua classificação é I')

