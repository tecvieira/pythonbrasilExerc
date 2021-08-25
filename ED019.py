unidade = ('', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezena = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sesseta', 'setenta', 'oitenta', 'noventa')

centenas = ('', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
            'setecentos', 'oitocentos', 'novecentos')

print('-'*45)
print('LEIA POR EXTENSO UM NÚMERO ENTRE 0 e 999'.center(45))
print('-'*45)
while True:
    num = int(input('- Digite um número: '))
    print(f'\033[35mO número {num} é escrito assim: ', end='')
    if num == 0:
        print('zero')
    elif num == 100:
        print('cem')
    else:
        if num > 100:
            print(centenas[int(str(num)[0])], end=' ')
            num = num - int(str(num)[0]) * 100
            if num != 0:
                print(' e', end=' ')
        if 0 < num < 20:
            print(unidade[int(str(num))], end=' ')
            num = 0
        elif num >= 20:
            print(dezena[int(str(num)[0])], end=' ')
            num = num - int(str(num)[0]) * 10
            if num != 0:
                print('e', unidade[num])
            print('\033[m')
            pergunta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
            if pergunta != 'S':
                break
print('Finalizando....')
print()
print('\033[31mBy TecVander v1.5')
