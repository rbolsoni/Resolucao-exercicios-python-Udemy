# Exercicio 35 - comissão da venda

venda = int(input('Qual o valor da venda?'))

if venda < 20000:
    print(f'Sua comissão será de {400 + ((venda / 100) * 14)}')
if 40000 > venda >= 20000:
    print(f'Sua comissão será de {500 + ((venda / 100) * 14)}')
if 60000 > venda >= 40000:
    print(f'Sua comissão será de {550 + ((venda / 100) * 14)}')
if 80000 > venda >= 60000:
    print(f'Sua comissão será de {600 + ((venda / 100) * 14)}')
if 100000 > venda >= 80000:
    print(f'Sua comissão será de {650 + ((venda / 100) * 14)}')
if venda > 100000:
    print(f'Sua comissão será de {700 + ((venda / 100) * 16)}')

