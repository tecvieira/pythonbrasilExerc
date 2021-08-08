from textopython.lib2.interface2 import *
from textopython.lib2.arquivo2 import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar pessoas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:  # opção listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')  # opção 2 cadastrar nova pessoa.
        nome = str(input('Nome: '))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida.')
    sleep(2)
