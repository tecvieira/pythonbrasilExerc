print('**** CALCULE SEU PESO IDEAL ****')
nome = str(input('Informe seu nome: ')).strip().upper()
altura = float(input('Informe sua altura:'))
sexo = str(input('Informe o seu sexo: use M ou F')).strip().upper()
if sexo == 'M':
    idealpeso = (72.7 * altura) - 58
    print(f'{nome} o seu peso ideal é {idealpeso:.2f}')
elif sexo == 'F':
    idealpeso = (62.1 * altura) - 44.7
    print(f'{nome} o seu peso ideal é {idealpeso:.2f}')
print()
print('Cuide bem da sua saúde.')