# Exercicio 18

import sys

num = int(input('Digite o tipo de operação a ser realizada: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 Divisão'))
if num == 1:
    soma1 = float(input('Digite um numero:'))
    soma2 = float(input('Digite outro numero:'))
    soma_total = soma1 + soma2
    print('O valor da soma é:', soma_total)
    sys.exit()
elif num == 2:
    sub1 = float(input('Digite um numero:'))
    sub2 = float(input('Digite outro numero:'))
    sub_total = sub1 - sub2
    print('O valor da subtração é:', sub_total)
    sys.exit()
elif num == 3:
    mul1 = float(input('Digite um numero:'))
    mul2 = float(input('Digite outro numero:'))
    mul_total = mul1 * mul2
    print('O valor da multiplicação é:', mul_total)
    sys.exit()
elif num == 4:
    div1 = float(input('Digite um numero:'))
    div2 = float(input('Digite outro numero:'))
    div_total = div1 / div2
    print('O valor da divisão é:', div_total)
    sys.exit()
else:
    print('Numero invalido. Digite um valor de 1 a 4 no menu.')
