# Exercicio 19

num = int(input('Digite um valor para saber se é divisivel por 5 ou por 3:'))
div3 = num % 3
if div3 == 0:
    print('Esse numero é divisivel por 3.')

div5 = num % 5
if div5 == 0:
    print('Esse numero é divisivel por 5.')

else:
    print('Esse numero não é divisivel por 3 e nem por 5')