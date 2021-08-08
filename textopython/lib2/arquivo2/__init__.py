from textopython.lib2.interface2 import cabecalho


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')  # abre arquivo
        a.close()  # fecha arquivo
    except FileNotFoundError:  # tratamento de Erro
        return False  # se não encontrar False
    else:
        return True  # se abrir e fechar True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # se não exite crie (wt+)
        a.close()
    except:
        print('Houve um ERRO, na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    global a  # não tem na aula
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # apend text (at)
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')  # acrescentar os dados
        except:
            print('Houve ERRO na escrita de dados.')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
