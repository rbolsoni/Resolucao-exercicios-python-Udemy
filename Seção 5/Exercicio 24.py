# Exercicio 24 - taxa de imposto

v = int(input('Digite o valor do produto:'))
estado = int(input('Digite o estado: 1-MG, 2-SP, 3-RJ e 4-MS'))
if estado < 1 or estado > 4:
    print('Digite um numero de estado valido!')
elif estado == 1:
    vmg = v + (v / 100 * 7)
    print('O valor do produto é:', vmg)
elif estado == 2:
    vsp = v + (v / 100 * 12)
    print('O valor do produto é:', vsp)
elif estado == 3:
    vrj = v + (v / 100 * 15)
    print('O valor do produto é:', vrj)
elif estado == 4:
    vms = v + (v / 100 * 8)
    print('O valor do produto é:', vms)
