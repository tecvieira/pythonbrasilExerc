from time import sleep

frase = str(input('Informe uma frase:'))
frase1 = str(input('Informe outra frase:'))
print('-' * 45)
print('Analizando frazes sugeridas...'.center(45))
print('-'*45)
sleep(1)
print(f'Frase - 1: {frase} ')
print(f'Frase - 2: {frase1}')
print('-'*45)
if len(frase) == len(frase1):
    print('As duas frases possuem o mesmo tamanho.')
    print(f'As frases posssuem {len(frase)} caracteres.')
    if frase.split() == frase1.split():
        print(' As frases possuem mesmo conteudo')
    else:
        print('Apesar do mesmo tamanho, o contúdo das frases são diferente.')

else:
    print('As frases possuem tamanhos diferentes.')
    print(f'A primeira frase possui {len(frase)} caracteres.')
    print(f'A segunda frase possui {len(frase1)} caraacteres.')
    if frase.split() != frase1.split():
        print(' As frases possuem contúdos diferentes')
print('-'*3)
print('fim')
