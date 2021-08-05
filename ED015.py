def triangulo() -> str:
    if ladoA<ladoB+ladoC and ladoC<ladoA+ladoB and ladoB<ladoA+ladoC:
        return 'É UM TRIÂNGULO'
    else:
        return 'NÃO É UM TRIANGULO'


def tipoTriang() -> str:
    if ladoA < ladoB + ladoC and ladoC < ladoA + ladoB and ladoB < ladoA + ladoC:
        if ladoA == ladoB != ladoC or ladoC==ladoB != ladoA or ladoA == ladoC != ladoB:
            return 'TIPO ISÓSCELES'
        if ladoA != ladoB != ladoC:
            return 'TIPO ESCALENO'
        if ladoA == ladoB == ladoC:
            return 'TIPO EQUILÁTERO'
    else:
        return 'Medidas incorretas'


print('*'*45)
print('ANALISADOR DE TRIÂNGULOS'.center(45))
print('*'*45)
ladoA = float(input('Tamanho do lado "A" : '))
ladoB = float(input('Tamanho do lado "B" :'))
ladoC = float(input('Tamanho do lado "C" : '))
print('-'*45)
print(f'Com as medidas informadas {ladoA}, {ladoB} e {ladoC} após analise comclui-se:\n{triangulo()} - {tipoTriang()}.')
