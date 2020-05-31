# Exercicio 52 - Amigos jogaram na loteria

p1 = int(input('Quando o Jogador 1 pagou? '))
p2 = int(input('Quando o Jogador 2 pagou? '))
p3 = int(input('Quando o Jogador 3 pagou? '))
premio = int(input('Qual o valor total do premio? '))

soma = premio / (p1 + p2 + p3)

j1 = p1 * soma
j2 = p2 * soma
j3 = p3 * soma

print(f'O jogador 1 receberá R$ {j1}')
print(f'O jogador 2 receberá R$ {j2}')
print(f'O jogador 3 receberá R$ {j3}')

