print('*'*45)
print('LOJA TABAJARA S/A'.center(45))
print('*'*45)
salario = 0
indice = 0
reajuste = 0
while True:
    salario = float(input('Informe o salário antigo: R$'))
    print('-'*45)
    if salario <= 280:
        reajuste = salario * 20 / 100
        indice = int(20)
    if 281 <= salario <= 700:
        reajuste = salario * 15 / 100
        indice = int(15)
    if 701 <= salario <= 1500:
        reajuste = salario * 10 / 100
        indice = int(10)
    if salario > 1500:
        reajuste = salario * 5 / 100
        indice = int(5)

    print(f'SALÁRIO ANTIGO:                   R$ {salario:.2f}')
    print(f'\033[34mPercentual concedido:                   {indice}%\033[m')
    print(f'REAJUSTE                           R$ {reajuste:.2f}')
    print('-'*45)
    print(f'\033[34mNOVO SALÁRIO                      R$ {salario+reajuste:.2f}\033[m')
    pergunta = str(input('\033[31mDeseja novo cálculo? [S/N]\033[m')).strip().upper()[0]
    if pergunta == 'N':
        break
print('\033[32mFim...\033[m')
