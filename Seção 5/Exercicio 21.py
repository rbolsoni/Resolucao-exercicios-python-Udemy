# Exercicio 21 - Operações

var = float(input('Esolha uma opção: \n'
                  '1 - Soma de dois numeros \n'
                  '2 - Diferença entre dois numeros \n'
                  '3 - Produtos entre dois numeros \n'
                  '4 - Divisão entre dois numeros \n'
                  ''))
if var == 1:
    soma1 = float(input('Digite um valor:'))
    soma2 = float(input('Digite outro valor:'))
    print(f'A soma dos numeros {soma1} + {soma2} é {soma1 + soma2}')

if var == 2:
    sub1 = float(input('Digite um valor:'))
    sub2 = float(input('Digite outro  valor:'))
    print(f'A soma dos numeros {sub1} + {sub2} é {sub1 - sub2}')

if var == 3:
    mult1 = float(input('Digite um valor:'))
    mult2 = float(input('Digite outro  valor:'))
    print(f'A soma dos numeros {mult1} + {mult2} é {mult1 * mult2}')

if var == 4:
    div1 = float(input('Digite um valor:'))
    div2 = float(input('Digite outro  valor:'))
    print(f'A soma dos numeros {div1} + {div2} é {div1 / div2}')

else:
    print('Numero invalido! Digite um numero de 1 a 4.')
