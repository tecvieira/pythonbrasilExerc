def calcHora():
    if salario > 0:
        return salario /220


salario = float(input('Informe seu salário bruto: R$'))
print(f'O valor da hora trabalhada e R${calcHora():.2f}.')