# Exercicio 10 - Peso ideal

alt = float(input('Digite a altura em metros:'))
sexo = bool(input('Digite o sexo: (m)Masculino e (f)Feminino.'))
m = True
f = False
hom = float(72.7 * alt) - 58
mul = float(62.1 * alt) - 44.7
if sexo is True:
    print('O peso ideal para homens com,', alt, 'm é de', hom)
elif sexo is True:
    print('O peso ideal para mulheres com,', alt, 'm é de', mul)
else:
    print('Digite o sexo somente com m ou f')
