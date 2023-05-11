print('**** conversor de temperatura  °C x °F ****')
tempconv = 0
escala = ''
while True:
    temp = float(input('Informe a temperatura:'))
    escala = str(input('Em qual escala está esta temperatura? use F ou C: ')).strip().upper()
    while escala not in 'FC':
        print('\033[31mERRO! digite F ou C.\033[m')
        escala = str(input('Em qual escala está esta temperatura? use F ou C: ')).strip().upper()
    if escala == 'F':
        tempconv = 5 * ((temp - 32) / 9)
        print(f'O valor em gráus Celsius é: {tempconv:.2f}°C')
    elif escala == 'C':
        tempconv = (1.8 * temp) + 32
        print(f'O valor em Fahrenheit é: {tempconv:.2f}°F')
    print()
    resp = str(input('Do you wish to continue, type it S/N')).strip().upper()
    while resp not in 'SN':
        print('\033[31mInvalid answer, type it S ou N\033[m')
        resp = str(input("Do you wish to continue, S/N"))
    if resp == 'N':
        break
print()
print('\033[33mFinish... By TecVander.')
