from datetime import datetime
from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO, digite número inteiro.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n Usuário não digitou um número')
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção:')
    return opc


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do Arquivo!\033[m')
    else:
        print(f'\033[34mArquivo {datatext()} criado com sucesso!\033[m')


def lerArquivo(nome):
    global a
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler arquivo!\033[m')
    else:
        cabecalho('GLICEMIA , DATA , HORA')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<3}{dado[1]:>20}')
    finally:
        a.close()


def cadastrar(arq, leitura='não informada', datahora=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{leitura} ; { datatext()}\n')
        except:
            print('\033[31mHouve ERRO na escrita de dados!')
        else:
            print(f'\033[34mNovo registro de {datatext()} adicionado.\033[m')
            a.close()


def datatext():
    data = datetime.now()
    datatext = data.strftime(', %d/%m/%Y , %H:%M ')
    return datatext


arq = 'glicemia2nova.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver mediçoes cadastradas", "Cadastrar nova medição", "Sair do sistema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO REGISTRO')
        leitura = leiaInt('Medição Atual:')
        datatext()
        cadastrar(arq, leitura, datatext())
    elif resposta == 3:
        sleep(1)
        cabecalho('\033[32mSaindo do sistema...')
        sleep(1)
        print('Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida. \033[m')

