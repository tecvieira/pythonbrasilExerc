#analiza a resposta e em caso de erro informa
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


#função para criar linhas automáticas com tamanho 42
def linha(tam=45):
    return '-' * tam


#criando cabeçalho de forma automática.
def cabecalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())

#faz o cabeçalho tomar forma e pergunta opção
def menu(lista):
    cabecalho('Memu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção:')
    return opc
