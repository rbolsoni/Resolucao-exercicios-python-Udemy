# Exercicio 26 - consumo do carro

km = float(input('Digite a distancia em km:'))
cons = float(input('Digite a quantidade de litros consumidos:'))
kml = km / cons
if kml < 8:
    print('Venda o carro!')
elif 8 < kml < 14:
    print('Economico!')
elif kml > 14:
    print('Super economico!')
