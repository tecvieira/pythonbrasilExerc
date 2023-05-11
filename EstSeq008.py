print('*** CALCULANDO SALÁRIO MENSAL ***')
valhora = float(input('Informe o valor da hora trabalhada: '))
qthora = float(input('Quantas horas trabalhadas por dia?'))
qtdias = int(input('Quantos dias trabalhados?'))
print(f""" Recibo
{qthora} horas trabalhadas
R${valhora} valor da hora
R${(valhora * qthora) * qtdias}""")
