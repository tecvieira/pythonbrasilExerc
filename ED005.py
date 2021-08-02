nota1 = float(input('Informe a nota da primeira prova: '))
nota2 = float(input('Informe a nota da segunda prova: '))

media = (nota1 + nota2) / 2
if 9.99 >= media >= 7.0:
    print(f'\033[32mO aluno com média {media:.2f} está APROVAD0.\033[m')
elif media < 7:
    print(f'\033[31mO aluno com média {media:.2f} está REPROVADO\033[m')
elif media >= 10:
    print(f'\033[34mO aluno com média {media:.2f} está APROVADO COM DESTINÇÃO\033[m')
print('-'*45)
print('Sempre busque aprender mais, pense no futuro.')
