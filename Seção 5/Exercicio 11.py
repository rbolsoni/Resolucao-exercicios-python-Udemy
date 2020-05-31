# Exercicio 11 - soma dos algarismos

numi = int(input('Digite um numero:'))
if numi < 0:
    print('Numero Invalido!')
else:
    num0 = numi // 1 % 10
    num1 = numi // 10 % 10
    num2 = numi // 100 % 10
    num3 = numi // 1000 % 10
    soma = num0 + num1 + num2 + num3
    print('O valor da soma dos algarismos é:', soma)

