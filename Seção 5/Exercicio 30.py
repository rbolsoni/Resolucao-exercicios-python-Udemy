"""
Faça uma programa que receba 3 numeros e os mostre-os em ordem crescente
"""

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero:'))
num3 = int(input('Digite um numero:'))

lista = [num1, num2, num3]
lista.sort()
print(lista)