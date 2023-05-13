from time import sleep


somaidade = 0
media = 0
idadehomemvelho = 0
nomevelho = ''
mulher20menos = 0
for pess in range(1, 5):
    print(f'______{pess}º pessoa _______' )
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo, digite apenas [M/F]')).strip().upper()
    while sexo  not in 'MF':
        print('\033[31mERRO! digite apenas M ou F.\033[m]')
        sexo = str(input('Informe o sexo, digite M (masculino) ou F(feminino):')).strip().upper()
    somaidade = somaidade + idade
    media = somaidade / pess
    if pess == 1:
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in 'M' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        mulher20menos += 1
print(f'\033[34mA média de idade das pessoas informadas é {media} anos.')
print(f'O {nomevelho} é o homem mais velho com {idadehomemvelho} anos.')
print(f'Temos {mulher20menos} mulher(es) com menos de 20 anos.\033[m]')
print('\033[31mfinalizando.....\033[m]')
sleep(3.0)
print('\033[32mByTecVander')
