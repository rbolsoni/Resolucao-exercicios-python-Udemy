# Exercicio 13 - media ponderada

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

mediap = (((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / (1 + 1 + 2))
print('A media ponderada do aluno é', mediap)
if mediap > 6:
    print('O aluno foi aprovado!')
else:
    var = mediap < 6
    print('O aluno foi reprovado!')

