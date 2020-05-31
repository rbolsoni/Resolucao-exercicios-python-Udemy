# Exercicio 8 - Media de notas
import sys

num1 = float(input('Digite uma nota do aluno:'))
if num1 > 10:
    sys.exit(print('Digite um numero de 0 a 10.'))

num2 = float(input('Digite outra nota do aluno:'))
if num2 > 10:
    sys.exit(print('Digite um numero de 0 a 10.'))

num3 = (num1 + num2) // 2
print('A nota média é:', num3)
