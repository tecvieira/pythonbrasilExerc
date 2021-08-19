from datetime import date
print('_'*35)
print('Verifique se o ano é bissexto:'.center(35))
print('-'*35)
ano = int(input('Informe o ano a ser analisado:'))
if ano == 0:
    ano = date.today().year
    print(f'O ano atual é {ano}.')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} analisado é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
