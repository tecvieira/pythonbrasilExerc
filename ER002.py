print('-' * 45)
print('NOVO USUÁRIO, CADASTRE USUÁRIO E SENHA.'.center(45))
print('-' * 45)
while True:
    login = str(input('Nome de usuário:')).strip().upper()
    senha = str(input('Informe sua senha:')).strip()
    segur = str(len(senha) * '*')
    if senha == login:
        print('Usuário e senha devem ser diferentes.')
    else:
        break
print(f'\033[35mUsuário: {login}  senha:{segur}, cadastrados com sucesso!')