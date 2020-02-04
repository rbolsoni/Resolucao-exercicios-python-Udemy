# Exercicio 49 - experiencia biologica

h = int(input('Digite a hora:'))
m = int(input('Digite o minuto:'))
s = int(input('Digite o segundo:'))
t = int(input('Digite o tempo do experimento em segundos:'))

th = t // 3600
tm = (t % 3600) / 60
ts = ((t % 3600) % 60)

hn = h + th
mn = m + tm
sn = s + ts

print('A hora de termino do experimento será: {:.0f} horas, {:.0f} minutos\
 e {:.0f} segundos'.format(hn, mn, sn))
