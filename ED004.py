letra = str(input('Digite uma letra e verifique se é uma vogal ou consoante: '))
vogal = ['A','a', 'E', 'e', 'I','i', 'O','o', 'U','u']
if letra not in vogal:
    print(f'A letra digitada {letra} é uma consoante.')
else:
    print(f'A letra digitada {letra} é uma vogal.')
