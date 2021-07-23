aluno = str(input('Informe o nome do aluno:'))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota:'))
nota4 = float(input('Quarta nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('-' * 15)
print(f'Aluno: {aluno}')
print('-' * 15)
print(f'Para as seguintes notas: {nota1}, {nota2}, {nota3}, {nota4} sua média foi {media:.2f}. ')
if media <= 5:
    print('REPROVADO')
elif 5 <= media <= 7:
    print('RECUPERAÇÃO')
else:
    print('Aprovado!!!')
