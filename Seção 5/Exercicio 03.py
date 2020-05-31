# Exercicio 3 - positivo raiz quadrada e negativo ao quadrado

num1 = float(input('Digite um numero:'))
if num1 > 0:
    num1 = num1 ** 0.5
    print('O resultado é:', num1)
elif num1 < 0:
    num1 = num1 ** 2
    print('O resultado é:', num1)
else:
    print('Esse numero é invalido.')
