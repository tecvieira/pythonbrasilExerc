while True:
    resp = int(input('Informe uma nota entre 0 e 10:'))
    if resp > 10 or resp < 0:
        print('\033[31mERRO! digite uma opção válida.\033[m')
    else:
        break
if resp <= 4:
    print(f'\033[31mA sua nota é {resp}, está reprovado.\033[m')
elif 5 <= resp <= 7:
    print(f'\033[33mA sua nota é {resp}, está de recuperação.\033[m')
elif resp >= 8:
    print(f'\033[34mParabéns sua nota é {resp} você foi aprovado.')
print('Fim...')
