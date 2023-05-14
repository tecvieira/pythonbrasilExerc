from random import randint
from time import sleep

computador = randint(1, 10)
acertou = False
palpite = 0
print('\033[32m**********Tente advinhar qual o número de 1 a 10 sorteado pelo computador.*********\033[m')
print('\033[34mSorteando....\033[m')
sleep(2.0)
while not acertou:
    jogador = int(input('Qual o seu palapite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS....  Tente outra vez.')
        elif jogador > computador:
            print('MENOS....  Tente outra vez.')
print(f'\033[34mAcertou...... com {palpite} palapites.')
