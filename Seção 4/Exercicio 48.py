# Exercicio 48 - Convertendo segundos

vs = int(input('Digite o valor em segundos:'))
vh = vs // 3600
vm = (vs % 3600) / 60
vs2 = ((vs % 3600) % 60)

print('O valor dos segundos {} é = {:.0f} horas, {:.0f} minutos e {:.0f} segundos'.format(vs, vh, vm, vs2))
