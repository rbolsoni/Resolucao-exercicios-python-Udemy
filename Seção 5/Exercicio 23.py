# Exercicio 23 - ano bissexto

ano = int(input('Digite o ano para saber se é bissexto:'))
ano400 = ano % 400
ano4 = ano % 4
ano100 = ano % 100
ano_resul = ano4 + ano100

if ano400 == 0:
    print('Esse ano é bissexto!')
elif ano400 == 1 or ano4 != 0 or ano_resul == 0:
    print('Esse ano não é bissexto!')
elif ano_resul != 0:
    print('Esse ano é bissexto!')
