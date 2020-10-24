# Exercicio 33 - Produto barato ou caro

va = float(input('Qual o valor antigo?'))

if va < 50:
    vn = va + ((va / 100) * 5)
    print(f'Esse produto custa agora {vn:.2f}')
    if vn < 80:
        print('Esse produto está barato')
    elif 80 < vn < 120:
        print('Esse produto está normal')
    elif 120 < vn < 200:
        print('Esse produto está caro')
    elif 200 < vn:
        print('Esse produto está muito caro')
if 50 < va < 100:
    vn = va + ((va / 100) * 10)
    print(f'Esse produto custa agora {vn:.2f}')
    if vn < 80:
        print('Esse produto está barato')
    elif 80 < vn < 120:
        print('Esse produto está normal')
    elif 120 < vn < 200:
        print('Esse produto está caro')
    elif 200 < vn:
        print('Esse produto está muito caro')
if va > 100:
    vn = va + ((va / 100) * 15)
    print(f'Esse produto custa agora {vn:.2f}')
    if vn < 80:
        print('Esse produto está barato')
    elif 80 < vn < 120:
        print('Esse produto está normal')
    elif 120 < vn < 200:
        print('Esse produto está caro')
    elif 200 < vn:
        print('Esse produto está muito caro')