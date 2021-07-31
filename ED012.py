def irpf():
    if salario <= 900.00:
        return salario
    if 900.01 <= salario <= 1500.00:
        return salario * 5.0 / 100
    if 1500.01 <= salario <= 2500.00:
        return salario * 10 / 100
    if salario >= 2500.01:
        return salario * 20 / 100


def sindicato():
    if salario != 0:
        return salario * 3 /100


def fgts():
    if salario != 0:
        return salario * 11 /100


def calculo():
    saLiquid = salario - irpf() -sindicato()
    return saLiquid

nome = str(input('Nome do funcionário:')).strip().upper()
hora = int(input('Quantidade de horas trabalhada: '))
valHora = float(input('Informe valor da hora: R$ '))
salario = hora * valHora
print('*'*45)
print('LOJAS TABAJARAS S/A'.center(45))
print('*'*45)
print('Comprovante de Pagamento.'.center(45))

print(f'Salário Bruto                     R$ {salario:.2f}')
print(f'Desconto do IRPF:                 R$ {irpf():.2f}')
print(f'Contribuição sindical 3%          R$ {sindicato():.2f}')
print(f'\033[31mTotal de descontos                R$ {sindicato()+irpf():.2f}\033[m')
print('-'*45)
print(f'Salário Líquido (a receber)       R$ {calculo():.2f}')
print('-'*45)
print(f'FGTS recolhido 11%:               R$ {fgts():.2f}')
print()
print('-'*45)
print(f'{nome}'.center(45))

