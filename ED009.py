listanum = []
print('Organize em ordem decrescente seus palpites.'.center(45))
print('-'*45)
for c in range(0, 3):
    listanum.append(int(input(f'Digite um valor na posição {c}:')))
    listanum.sort(reverse=True)
print('-'*45)
print(f'\033[32mO números sugeridos foram {listanum[0],listanum[1],listanum[2]}')
