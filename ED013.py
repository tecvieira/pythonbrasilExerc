dia = ('0- Domingo', '1- Segunda', '2- Terça', '3- Quarta', '4- Quinta', '5- sexta', '6- Sábado')

while True:
    num = int(input('Escolha um número de 0 a 6 e descubra um dia da semana:'))
    if 0 <= num <= 6:
        print(f'Voce digitou o número {dia[num]}')
    if 0 < num > 6:
        print('Número inválido! Digite uma opção válida:')
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Até logo....')

