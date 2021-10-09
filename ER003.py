print('-' * 45)
print('Cadastro de Alunos da Academia'.center(45))
print('-' * 45)

nome = str(input('Nome:')).strip()
if len(nome) <= 3:
    print('ERRO! o nome deve ser maior que 3 caracteres.')
idade = int(input('Idade:'))
if 0 != idade <= 150:
    print('Idade está incorrect.')


