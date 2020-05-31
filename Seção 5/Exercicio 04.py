# Exercicio 4 - raiz quadrada e ao quadrado

num1 = float(input('Digite um numero:'))
if num1 <= 0:
    print('Por favor, digite um numero positivo!')
else:
    num2 = num1 ** 2
    num3 = num1 ** 0.5
    print('O numero ao quadrado é:', num2)
    print('A raiz quadrada do numero é:', num3)
