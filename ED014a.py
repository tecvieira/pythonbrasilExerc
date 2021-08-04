def media():
    media = (nota1 + nota2) / 2
    return media


def resultado() ->str:
    if media() >= 9:
        return 'NOTA - A, (APROVADO)'
    if 7.5 <= media() < 9:
        return 'NOTA - B, (APROVADO)'
    if 6.0 <= media() <7.5:
        return 'NOTA - C, (APROVADO)'
    if 4.0 <= media() < 6.0:
        return 'NOTA - D, (REEPROVADO)'
    if 0 <= media() <4.0:
        return 'NOTA - E, (REPROVADO)'


print('*'*45)
print('COLÉGIO MARECHAL LOTH'.center(45))
print('*'*45)
print('Avaliação de alunos'.center(45))
print('-'*45)
nome = str(input('Nome do aluno: ')).strip().upper()
nota1 = float(input('Nota do primeiro semestre: '))
nota2 = float(input('Nota do segundo semestre:'))
print(f'O aluno {nome}, com notas {nota1} e {nota2:.2f} obteve média {media()}.')
print(f'O aluno com {resultado()}.')