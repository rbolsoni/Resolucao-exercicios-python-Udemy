# Exercicio 43 - Programa para vendedores

valor_total = float(input('Digite o valor total do produto:'))
valor_desconto = valor_total-((valor_total/100)*10)
valor_parcelado = valor_total/3
com_vista = (valor_desconto/100)*5
com_parcelado = (valor_total/100)*5

print('O valor do produto com pagamento a vista e desconto é: R$', valor_desconto)
print('O valor das parcelas desse produto é: R$', valor_parcelado)
print(' O valor da comissão para o produto a vista é: R$', com_vista)
print('O valor da comissão para o produto parcelado é: R$', com_parcelado)