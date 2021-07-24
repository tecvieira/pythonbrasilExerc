def irDesc():
    return salario * 11/100


def sindicato():
    return salario * 5/100

def inss():
    return salario * 8/100


def totDesc():
    return inss() + sindicato() + irDesc()

def salLiquido():
    return salario - totDesc()


print('-'*40)
print('Comprovante de Pagamento'.center(40))
print('-'*40)
while True:
    valhora = float(input('Informe valor da hora: R$ '))
    hora = float(input('total de horas trabalhadas:'))
    salario = float(valhora * hora)
    print(f'Salário Bruto   -  R${salario:.2f}')
    print(f'IR (11%)           R${irDesc():.2f}')
    print(f'INSS (8%):         R${inss():.2f}')
    print(f'Cont.Sindical(5%): R${sindicato():.2f}')
    print(f'Total descontos -  R${totDesc():.2f}')
    print('-' * 40)
    print(f'Líquido a Receber: R${salLiquido():.2f} ')
    print('-' * 40)
    pergunta = str(input('Deseja novo calculo, [S/N]')).strip().upper()
    if pergunta == 'N':
        break
print('\033[32mVolte sempre!!!'.center(40))
