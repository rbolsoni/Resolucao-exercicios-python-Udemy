# Exercicio 9 - Emprestimo

sal = float(input('Digite o valor do salario:'))
prest = float(input('Digite o valor da prestação:'))
porce = sal / 100 * 20
if prest > porce:
    print('Emprestimo não concedido.')
else:
    print('Emprestimo concedido.')
