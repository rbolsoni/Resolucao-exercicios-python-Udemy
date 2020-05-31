#Exercicio 53 - Preço da tela no terreno

comp = float(input('Digite o comprimento do terreno: '))
larg = float(input('Digite a largura do terreno: '))
m = comp * larg

preco = float(input('Digite o preço do metro da tela: '))
custo = m * preco

print(f'O custo para cercar o terreno com tela é: R${custo}')

