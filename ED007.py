print('-' * 45)
print('DESCUBRA O MAIOR E O MENOR NÚMERO.'.center(45))
print('-' * 45)
num = int(input('primeiro número:'))
num1 = int(input('segundo número'))
num2 = int(input('terceiro número'))
maior = num
if num1 > num and num1 > num2:
    maior = num1
if num2 > num and num2 > num1:
    maior = num2
menor = num
if num1 < num and num1 < num2:
    menor = num1
if num2 < num and num2 < num1:
    menor = num2
print('-' * 45)
print(f'\033[33mO maior número informado foi {maior}'.center(45))
print(f'O menor número informado foi {menor}\033[m'.center(45))
print('-' * 45)
