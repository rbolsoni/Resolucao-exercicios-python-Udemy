# Exercicio 28 - prova de soma

import sys

# Numeros aleatorios
q1_num1 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 > 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q1_num2 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q2_num1 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q2_num2 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q3_num1 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q3_num2 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q4_num1 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q4_num2 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q5_num1 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))
q5_num2 = int(input('Digite um numero de 1 a 100:'))
if 1 > q1_num1 < 100 and type != int:
    sys.exit(print('Numero invalido! O numero deve estar entre 1 e 100!'))

r1 = q1_num1 + q1_num2
r2 = q2_num1 + q1_num2
r3 = q3_num1 + q3_num2
r4 = q4_num1 + q4_num2
r5 = q5_num1 + q5_num2

# Inicio da prova

p1 = int(input('Qual a soma de {} + {}?'.format(q1_num1, q1_num2)))
p2 = int(input('Qual a soma de {} + {}?'.format(q1_num1, q1_num2)))
p3 = int(input('Qual a soma de {} + {}?'.format(q1_num1, q1_num2)))
p4 = int(input('Qual a soma de {} + {}?'.format(q1_num1, q1_num2)))
p5 = int(input('Qual a soma de {} + {}?'.format(q1_num1, q1_num2)))

print('A soma de {} + {} é: {}'.format(q1_num1, q1_num2, r1))
print('A soma de {} + {} é: {}'.format(q2_num1, q2_num2, r2))
print('A soma de {} + {} é: {}'.format(q3_num1, q3_num2, r3))
print('A soma de {} + {} é: {}'.format(q4_num1, q4_num2, r4))
print('A soma de {} + {} é: {}'.format(q5_num1, q5_num2, r5))


rf = 0
if p1 == r1:
    rf = rf + 1
if p2 == r2:
    rf = rf + 1
if p3 == r3:
    rf = rf + 1
if p4 == r4:
    rf = rf + 1
if p5 == r5:
    rf = rf + 1
    print('Você acertou {} questões'.format(rf))
else:
    print('Você errou todas as questões.')
