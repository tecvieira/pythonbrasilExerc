print('-' * 45)
print('COTAÇÃO DE PREÇOS.'.center(45))
print('-' * 45)
produto = str(input('Informe o produto analisado:'))
preco = float(input('Informe o primeiro valor, R$:'))
preco1 = float(input('Informe o segundo valor, R$'))
preco2 = float(input('Informe o terceiro valor, R$'))
menor = preco
if preco1 < preco and preco1 < preco2:
    menor = preco1
if preco2 < preco and preco2 < preco1:
    menor = preco2
print(f'\033[34mO menor preço sugerido de {produto} foi R$ {menor}\033[m')
