print('PESQUISA DE HORÁRIO ESCOLAR')
print(('-' * 45))
while True:
    print('''
    M - MANHÃ
    T - TARDE
    N - NOITE
    ''')
    pergunta = str(input('Escolha M, T ou N, para informar seu horário escolar: ')).strip().upper()[0]
    if pergunta == 'M':
        print('Bom dia.')
    elif pergunta == 'T':
        print('Boa Tarde.')
    elif pergunta == 'N':
        print('Boa Noite.')
    elif pergunta not in 'MTN':
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    saida = str(input('Deseja continuar S/N')).strip().upper()[0]
    if saida == 'N':
        break
print('fim...')
