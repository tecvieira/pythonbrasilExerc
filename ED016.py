print('-'*55)
print('Calculando equação do segundo gráu:'.center(55))
print('Para o modelo abaixo, informe valores para a, b, c.'.center(55))
print('ax² + bx + c'.center(55))
print('-'*55)

while True:
    a = int(input('Informe o valor de "a" : '))
    if a == 0:
        print('\033[31m ERRO! Com "a" igual a zero esta equação não é do segundo gráu.\033[m')
        break
    b = int(input('Informe o valor de "b" :'))
    c = int(input('Informe o valor de "c" :'))
    d = (b ** 2 - (4 * a * c))
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    if d < 0:
        print(f'Valor de x1: {x1:.2f}')
        print(f'Valor de x2: {x2:.2f}')
        print(f'Para um DELTA {d}, (NEGATIVO) esta equação não possui raizes reais.')
        break
    elif d == 0:
        print(f'Valor de x1: {x1}')
        print(f'Valor de x2: {x2}')
        print(f'Para um DELTA = {d}, esta equação possui duas raizes reais.')
        break
    else:
        print(f'Valor do delta {d} ')
        print(f'Valor de x1: {x1}')
        print(f'Valor de x2: {x2}')
    pergunta = str(input('Deseja continuar? [S/N}')).strip().upper()[0]
    if pergunta == 'N':
        break
print('Até logo...')






