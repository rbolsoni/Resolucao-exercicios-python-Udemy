# Exercicio 19

import sys
import math

num = int(input('Digite um valor para saber se é divisivel por 5 ou por 3:'))
div3 = num % 3
if div3 == 0:
    print('Esse numero é divisivel por 3.')
    sys.exit()

div5 = num % 5
if div5 == 0:
    print('Esse numero é divisivel por 5.')
    sys.exit()
