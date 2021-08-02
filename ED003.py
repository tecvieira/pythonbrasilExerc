while True:
    sexo = str(input('Informe o sexo, [M/ F]. ')).strip().upper()
    if sexo == 'M':
        print(f'Sexo informado: {sexo} - MASCULINO.')
    elif sexo == 'F':
        print(f'Sexo informado: {sexo} - FEMININO')
    elif sexo != 'M' or 'F':
        print('ERRO DIGITE UM SEXO VÁLIDO')
    pergunta = str(input('Deseja alterar sua opção? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
