# Exercicio 3 - positivo raiz quadrada e negativo ao quadrado

num1 = float(input('Digite um numero:'))
if num1 > 0:
    num2 = num1 ** 0.5
    print('O resultado é:', num2)
elif num1 < 0:
    num3 = num1 ** 2
    print('O resultado é:', num3)
else:
    num1 == 0
    print('Esse numero é invalido.')
