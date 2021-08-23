menor_20 = ['', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa']

centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos',
            'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
while True:
    numero = int(input('\033[34mDigite o número: \033[m'))
    if numero < 0 or numero > 999:
        print('\033[31mERRO! digite um número entre 0 e 999.\033[m')
    else:
        print(f'O número {numero} por extenso fica: ', end='')
        if numero == 100:
            print('cem')
        elif numero == 0:
            print('zero')
        else:
            if numero > 100:
                print(centenas[int(str(numero)[0])], end='')
                numero = numero - int(str(numero)[0])*100
                if numero != 0:
                    print(' e', end=' ')
            if numero < 20:
                print(menor_20[int(str(numero)[0])], end=' ')
                numero = 0
            elif numero >= 20:
                print(dezenas[int(str(numero)[0])], end=' ')
                numero = numero - int(str(numero)[0])*10
            if numero != 0:
                print('e', menor_20[numero])

