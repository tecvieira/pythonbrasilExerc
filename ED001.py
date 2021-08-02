num = int(input('Digite um número inteiro:'))
num2 = int(input('Digite outro número inteiro:'))
if num > num2:
    print(f'O primeiro número, {num} foi o maior.')
elif num2 > num:
    print(f'O segundo número, {num2} foi o maior.')
else:
    print(f'Os números informados são iguais {num}.')
