while True:
    nome = str(input('Informe seu nome: ')).strip().upper()
    altura = float(input('Informe sua altura: '))
    pesoatual = float(input('Informe seu peso atual: '))       
    print('''
    Menu de opções
    [1] PESO IDEAL MASCULINO
    [2] PESO IDEAL FEMININO
    [3] PESO IDEAL AJUSTADO
    [0] PARA SAIR
          ''')
    print()
    opcao = int(input('Escolha sua opção: '))
    while opcao < 0 or opcao > 3:
        print('ERRO! opçao inválida, escolha um valor do menu.')
        opcao = int(input('Escolha sua opção: '))
    if opcao == 1:
        pideal = 52 + (0.75 * (altura - 152.4))
        print(f'{nome}, o seu peso ideal é {pideal:.2f}')
    elif opcao == 2:
        pideal = 52 + (0.67 * (altura - 152.4))
        print(f'{nome}, o seu peso ideal é {pideal:.2f} ')
    elif opcao == 3:       
        sexo = str(input('Informe o sexo: digite M ou F ')).strip().upper()
        if sexo in 'M':
            pideal = 52 + (0.75 * (altura - 152.4))
            pajustado = ((pesoatual - pideal) * 0.25) + pideal
            print(f'{nome}, o seu peso ajustado é {pajustado:.2f}')
        elif sexo in 'F':
            pideal = 52 + (0.67 * (altura - 152.4))
            pajustado = ((pesoatual - pideal) * 0.25) + pideal
            print(f'{nome}, o seu peso ajustado é {pajustado:.2f}')
    elif opcao == 0:        
        break    
    resp = str(input('Deseja continuar? digite [S/N]')).strip().upper()    
    while resp not in 'SN':        
        print('ERRO! digite S ou N')
        resp = str(input('Deseja continuar? digite [S/N]')).strip().upper()
    if resp == 'N':
        break
print('Fim...')
