# Exercicio 29 - prova de matematica

from random import randint

c = 0
for contador in range(1, 6):
    a = randint(1, 100)
    b = randint(1, 100)
    conta = int(input(f'{contador}- Qual o valor da soma de {a} + {b}? ='))
    resul = a + b
    if conta == resul:
        print('Acertou acertou.')
        c += 1
    else:
        print('Infelizmente você errou.')
print(f'Você acertou {c} questões.')

