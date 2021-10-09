from datetime import datetime


def datatext():
    data = datetime.now()
    datatext = data.strftime(' %d/%m/%Y ; %H:%M hs. ')
    return datatext


print('-'*30)
print('Cotação de Preços'.center(30))
print('-'*30)
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome do fornecedor:')))
    temp.append(float(input('R$ ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja informar outro fornecedor? [S/N]'))
    if resp in 'Nn':
        break
print(f'O melhor preço é R$ {men:.2f} do fornecedor', end='')
for p in princ:
    if p[1] == men:
        print(f' {p[0]} - ', end='')
        print(datatext())
print()
