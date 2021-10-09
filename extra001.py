from datetime import date


def arqExiste(nomearq):
    try:
        a = open(nomearq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArq(nomearq):
    try:
        a = open(nomearq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nomearq} criado com sucesso!')


def lerArq(nomearq):
    try:
        a = open(nomearq, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        print('SERVIÇOS CADASTRADOS')
        for linha in a:
            dado = linha.split(' ; ')
            dado[4] = dado[4].replace('\n',' ')
            print(f'{dado[0]},{dado[1]},{dado[2]},{dado[3]},{dado[4]}')
    finally:
        a.close()


def cadastArq(nomearq, atual=date.today(), numero=0, modelo='desconhecido', defeito='não informado'):
    try:
        a = open(nomearq, 'at')
    except:
        print('Houve erro na abertura do arquivo')
    else:
        try:
            a.write(f'{atual};{numero};{modelo}; {defeito};\n')
        except:
            print('Houve ERRO na escrita de dados!')
        else:
            print(f'Novo registro de {numero} adicionado')
            a.close()


print('-' * 30)
print('Registro de Serviço'.center(30))
print('-' * 30)
opcao = 0
nomearq = 'vista.txt'
while opcao != 5:
    if not arqExiste(nomearq):
        criaArq(nomearq)
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
        lerArq(nomearq)
    elif opcao == 2:
        while True:
            data = date.today()
            # data = (f'{atual.day}/{atual.month}/{atual.year} ')
            numero = int(input('Número do equipamento:'))
            modelo = str(input('Equipamento modelo:')).strip().upper()
            defeito = str(input('Informe o defeito apresentado:')).strip().upper()
            cadastArq(nomearq)
            # print(f'\033[35m{data} - Modelo: {tipo} -  Equipamento Nº {registro} - Defeito informado: {defeitoIni}\033[m ')
            pergunta = str(input('Deseja novo cadastro? [S/N]')).strip().upper()[0]
            if pergunta != 'S':
                break
    elif opcao == 3:
        print('editar serviço cadastrado')
    elif opcao == 4:
        print('apagar registro.')
    elif opcao == 5:
        break

print('Saindo....')

#com erro para ler falta acabar

