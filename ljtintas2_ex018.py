import math

print('*'*45)
print('CALCULE O SUA TINTA'.center(45))
print('*'*45)
while True:
    area = float(input('Informe área que deseja pintar em m2: '))
    rendimento = 6
    tinta = math.ceil(area / rendimento)
    lata = int(tinta / 18)
    galao = int(tinta/ 3.6)
    print(f'\033[32mSão necessários {tinta} litros de tinta para pintar {area:.0f} m².\033[m')
    print('-' * 45)
    print('COMO DESEJA COMPRAR:'.center(45))
    print('-' * 45)
    print("""
    1 - Comprar apenas latas de 18 litros
    2 - Comprar apenas galões de 3,6 litros
    3 - Comprar latas e galões de acordo com necessidade.
    4 - sair
    """)
    pergunta = int(input('O que deseja fazer?'))
    if pergunta == 1:
        if tinta % 18 != 0:
            lata += 1
            print(f'compre {lata} lata(s) de 18 litros por R${(lata * 80)},00')
    elif pergunta == 2:
        if tinta % 3.6 != 0:
            galao += 1
            print(f'compre {galao} galão(ões) de 3,6 litros por R${(galao * 25)},00')

    elif pergunta == 3:
        mixlatas = int(tinta/ 18)
        mixgaloes = int((tinta - (mixlatas * 18)) / 3.6)
        if ((tinta -mixlatas * 18) % 3.6 != 0):
            mixgaloes += 1
            print(f'\033[32mCompre {mixlatas} lata(s) de 18 litros e {mixgaloes} galão(ões) de 3,6 litros\n'
                  f'no valor de R${(mixlatas*80)+(mixgaloes*25)},00\033[m')
            print()
    elif pergunta == 4:
        break
    print('\033[31m='*45)
    final = str(input('Deseja sair do sistema? [S/N]:')).strip( ).upper( )
    print('='*45)
    if final == 'S':
        break
print('Até logo!!!\033[m ')
