# Exercicio 6 - numero maior e a diferença

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))

if num1 > num2:
    print('O numero maior é:', num1)
elif num1 < num2:
    print('O numero maior é:', num2)

if num1 > num2:
    num3 = num1 - num2
else:
    num1 < num2
    num3 = num2 - num1

print('A difenreça entre os dois numeros é de:', num3)
