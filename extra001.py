from datetime import date
print('-'*30)
print('Registro de Serviço'.center(30))
print('-'*30)
opcao = 0
while opcao != 5:
    print('Escolha sua opção:')
    print("""
    01 - LISTAR SERVIÇOS
    02 - CADASTRAR NOVO SERVIÇO
    03 - EDITAR SERVIÇO CADASTRADO
    04 - APAGAR SERVIÇO
    05 - SAIR DO SISTEMA
    """)
    opcao = int(input('O que deseja fazer?'))
    if opcao <= 0 or opcao >= 6:
        print('\033[31mERRO!!! selecione uma opção válida.\033[m')
    elif opcao == 1:
        print('listar serviços')
    elif opcao == 2:
        while True:
            atual = date.today()
            data = (f'{atual.day}/{atual.month}/{atual.year} ')
            registro = int(input('Número do equipamento:'))
            tipo = str(input('Equipamento modelo:')).strip().upper()
            defeitoIni = str(input('Informe o defeito apresentado:')).strip().upper()
            print(f'\033[35m{data} - Modelo: {tipo} -  Equipamento Nº {registro} - Defeito informado: {defeitoIni}\033[m ')
            pergunta = str(input('Deseja novo cadastro? [S/N]')).strip().upper()[0]
            if pergunta != 'S':
                break
    elif opcao == 3:
        print('esditar serviço cadastrado')
    elif opcao == 4:
        print('apagar registro.')
    elif opcao == 5:
        break

print('Saindo....')
