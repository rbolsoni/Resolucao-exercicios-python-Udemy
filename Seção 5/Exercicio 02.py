# Exercicio 2 - Validade da raiz quadrada

num1 = float(input('Digite um numero para saber a raiz quadrada:'))
num_raiz = num1 ** 0.5
if num1 < 0:
    print('Este numero é invalido. Digite um numero positivo.')

elif num_raiz > float(0):
    print(num_raiz)

