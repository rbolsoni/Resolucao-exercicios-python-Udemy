# Exercicio 8 - Media de notas

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
if 10 >= nota_1 >= 0 and 10 >= nota_2 >= 0:
    media = (nota_1 + nota_2) / 2
    print(f'A média da nota é: {media}')
else:
    print('Digite um valor valido, acima de 0 e menor que 10.')

