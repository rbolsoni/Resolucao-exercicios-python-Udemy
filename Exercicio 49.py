# Exercicio 49 - experiencia biologica

hora = int(input('Digite a hora:'))
minu = int(input('Digite o minuto:'))
seg = int(input('Digite o segundo:'))
total_seg = int(input('Digite o tempo do experimento em segundos:'))

final_hora = total_seg // 3600
final_min = (total_seg % 3600) / 60
final_seg = ((total_seg % 3600) % 60)

novo_hora = hora + final_hora
novo_min = minu + final_min
novo_seg = seg + final_seg

print(f'A hora de termino do experimento será: {novo_hora} horas, {novo_min} minutos\
 e {novo_seg} segundos')

