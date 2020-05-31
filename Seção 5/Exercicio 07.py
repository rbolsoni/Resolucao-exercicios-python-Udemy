# Exercicio 7 - numero amior ou igual

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))

if num1 > num2:
    print(f'O numero maior é: {num1}')
elif num1 == num2:
    print('Os numeros são iguais')
else:
    print(f'O numero maior é: {num2}')

