# Exercicio 42 - Salario base

sal_base = float(input('Digite o valor do salario base:'))
sal_grat = (sal_base/100)*5
sal_impos = (sal_base/100)*7
sal_real = sal_base+sal_grat-sal_impos
print('O salario final será de: R$', sal_real)


