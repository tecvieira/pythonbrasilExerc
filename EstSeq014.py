print('**** Controle de Pescaria ****')
quilos = float(input('Total de pescado variados: '))
if quilos > 50:
    multa = (quilos - 50) * 4.00
    print(f'R$ {multa:.2f} Excesso do limite permitido referente {quilos - 50:.2f}Kg')
