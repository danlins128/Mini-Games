import random
import os

def limpar_console():
    sistema = os.name
    if sistema == 'posix': # Para linux
        os.system('clear')
    elif sistema == 'nt': # Para windows
        os.system('cls')
    else:
        pass

def barra():
    print('-' * 34)

numero = random.randint(1, 5)


barra()
print(f"{'Bem vindos ao Adivinhe o número!':^34}")
barra()

i = ''
tentativas = 3
for c in range(3):    
    
    print(f'Tente adivinhar o número\nVocê tem {tentativas} tentativas. (1-5)')
    
    i = input('Seu palpite é: ')

    if int(i) == numero:
        limpar_console()
        print('-' * 40)
        print(f'Você acertou! Parabéns, o número era {numero}!')
        print('-' * 40)
        break
    
    elif int(i) < numero:
        limpar_console()
        barra()
        print('Tente um número mais alto!')
        barra()
        tentativas -=1
    
    else:
        limpar_console()
        barra()
        print('Tente um número mais baixo!')
        barra()
        tentativas -=1
    
if tentativas == 0 and int(i) != numero:
    limpar_console()
    print(f'Você esgotou suas tentativas. O número era {numero}!')   
