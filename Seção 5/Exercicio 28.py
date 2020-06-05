# Exercicio 28 - programa de numeros inteiros e tipos de medias

x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
z = float(input('Digite o valor de Z: '))
media = float(input('Digite um valor para o tipo de média: \n'
                    '1 - Média Geometrica \n'
                    '2 - Média Ponderada \n'
                    '3 - Média Harmônica \n'
                    '4 Média Aritmética \n'))
if media == 1:
    media = (x * y * z) ** (1/3)
    print(f'A média Geometrica é: {media}')
elif media == 2:
    media = (x + 2 * y + 3 * z) / 6
    print(f'A media ponderada é: {media}')
elif media == 3:
    media = (1 / x) + (1 / y) + (1 / z) / 1
    print(f'A media harmônica é: {media}')
elif media == 4:
    media = (x + y + z) / 3
    print(f'A media aritmetica é: {media}')

