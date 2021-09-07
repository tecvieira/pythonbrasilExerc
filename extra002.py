from time import sleep
from datetime import date

def cadastrar(nomearq, equipamento='vista', defeito='não_informado'):
    arquivo = open(nomearq, 'a')
    arquivo.write(f'{equipamento};{defeito}, \n')
    print(f'Novo registro de {equipamento} adicionado.')
    arquivo.close()

print('-' * 30)
print('Registro de Serviço'.center(30))
print('-' * 30)
opcao = 0
nomearq = 'vista.txt'
while opcao != 3:
    print('Escolha sua opção:')
    print("""\033[34m
    01 - LISTAR SERVIÇOS
    02 - CADASTRAR NOVO SERVIÇO  
    03 - SAIR DO SISTEMA
    \033[m""")
    opcao = int(input('O que deseja fazer?'))
    if opcao <= 0 or opcao >= 4:
        print('\033[31mERRO!!! selecione uma opção válida.\033[m')
    elif opcao == 1:
        data_atual = date.today()
        datatext = (f'{data_atual.day}/{data_atual.month}/{data_atual.year}')
        print(f'\033[33mLISTAGEM DE SERVIÇOS {datatext}')
        print('  Equipamentos  - Defeitos\033[m')
        arquivo = open(nomearq, 'rt')
        for linha in arquivo:
            dado = (linha.split('; '))
            dado[0] = dado[0].replace('\n',' ')
            print(dado)
        arquivo.close()
    elif opcao == 2:
        print('CADASTRAR NOVO SERVIÇO')
        equipamento = str(input('Informe o tipo de equipamento:'))
        defeito = str(input('Defeito encontrado:'))
        cadastrar(nomearq, equipamento, defeito)
    elif opcao == 3:
        break
print('Saindo...')
sleep(1)
print('Até logo!!!')
