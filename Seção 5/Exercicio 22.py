# Exercicio 22 - aposentadoria

idade = float(input('Digite a idade do trabalhador: '))
tempo = float(input('Digite o tempo de serviço: '))

if idade > 65:
    print('Pode se aposentar!')

elif tempo > 30:
    print('Pode se aposentar!')

elif idade > 60 and tempo > 25:
    print('Pode se aposentar!')

else:
    print('Não pode se aposentar!')


