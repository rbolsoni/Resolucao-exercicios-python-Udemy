# Exercicio 17 - area de um trapezio

base_menor = float(input('Digite o valor da base menor:'))
if base_menor < 0:
    print('O valor deve ser maior que 0')

base_maior = float(input('Digite o valor da base maior:'))
if base_maior < 0:
    print('O valor deve ser maior que 0')

alt = float(input('Digite o valor da altura:'))
if alt < 0:
    print('O valor deve ser maior que 0')

area = (((base_maior + base_menor) * alt) / 2)
print('A area do trapezio é:', area)
