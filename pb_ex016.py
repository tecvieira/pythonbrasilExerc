def totTintas():
    return area / 3


def latasTotal():
    return round(totTintas()) / 18


def completaLata():
    if totTintas() // 18:
        return latasTotal()
    else:
        return latasTotal()+1


def custofinal():
    return round(completaLata()) * preco


from datetime import date
while True:
    nome = str(input('Nome do cliente:')).upper()
    area = float(input('Informe tamanho da área a ser pintada (m²):'))
    data = date.today()
    tinta = str(input('Tinta/ cor (codigo):'))
    preco = float(input('Galão de 18 litros preço R$'))
    print('='*30)
    print('TINTAS PYTHON BRASIL'.center(30))
    print('-'*30)
    print('Calculadora de Tintas'.center(30))
    print('='*30)
    print(f'Cliente:{nome}')
    print(f'Data: {data.day}/{data.month}/{data.year}')
    print(f'Tinta escolhida: {tinta} ')
    print()
    print(f'Necessário {totTintas():.1f} litros para pintar {area}m². ')
    print(f'Comprar {completaLata():.0f} latas de 18 litros.')
    print(f'Valor total = R${custofinal():.2f}')
    print()
    print('='*30)
    print()
    pergunta = str(input('\033[31mDeseja novo cálculo: [S/N]\033[m')).strip().upper()[0]
    if pergunta == 'N':
        break
print('\033[34mObrigado, volte sempre!')



