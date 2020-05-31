# Exercicio 14 - Medias ponderadas de notas

nota_lab = int(input('Digite aqui a nota do trabalho de laboratório:'))
nota_as = int(input('Digite aqui a nota da avaliação semestral:'))
nota_af = int(input('Digite aqui a nota da avaliação final:'))
mediap = (((nota_lab * 2) + (nota_as * 3) + (nota_af * 5)) / (2 + 3 + 5))
if mediap < 2.9:
    print('O aluno foi reprovado!')
elif mediap < 4.9:
    print('O aluno está de recuperação!')
else:
    print('O aluno está aprovado!')
print(mediap)