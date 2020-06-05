# Exercicio 20 - tipos de triangulos

a = float(input('Digite o valor de um lado do triangulo:'))
b = float(input('Digite o valor de um lado do triangulo:'))
c = float(input('Digite o valor de um lado do triangulo:'))
somaab = a + b
somaac = a + c
somabc = b + c
soma = a + b + c

if a > somabc:
    print('Numero é invalido!')

elif b > somaac:
    print('Numero é invalido!')

elif c > somaab:
    print('Numero é invalido!')


if a == b == c:
    print('Triangulo equilatero')
elif a == b:
    print('Triangulo isoceles')
elif a == c:
    print('Triangulo isoceles')
elif b == c:
    print('Triangulo isoceles')
else:
    print('Triangulo escaleno')

