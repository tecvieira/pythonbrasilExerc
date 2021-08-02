a = int(input('Informe um número: '))
b = int(input('Informe o segundo número:'))
c = int(input('Informe o último número:'))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'Os maior entre os números {a}, {b} e {c} e o {maior}.')
print(f'O menor entre os números acima é o {menor}.')
