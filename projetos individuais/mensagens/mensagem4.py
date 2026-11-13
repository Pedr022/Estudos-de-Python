import os
import time
os.system('')

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[H\033[J', end='')

def escrever(texto, cor=0):
    BRANCO = '\033[37m'
    PRETO = '\033[30m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    MAGENTA = '\033[35m'
        
    RESET = '\033[0m'

    cores = [BRANCO, PRETO, VERMELHO, VERDE, AMARELO, MAGENTA]

    return f'{cores[cor]}{texto}{RESET}'

def digitar(texto, cor):
    for char in texto:
        if char != ' ':
            time.sleep(0.01)
            print(escrever(char, cor), end='', flush=True)
        else:
            print(escrever(char, cor), end='', flush=True)

def getNameFile():
    return input('Digite o nome do arquivo: ')

def getCor():
    print('''
Escolha uma cor

|-----------------|
    0. Branco
    1. Preto
    2. Vermelho
    3. Verde
    4. Amarelo
    5. Magenta
|-----------------|
''')
    return int(input('>>> '))

while True:
    try:
        arquivo = open(getNameFile(), 'r')
        color = getCor()

        limparTerminal()
        for lin in arquivo.readlines():
            digitar(lin, color)

        arquivo.close()
        break

    except FileNotFoundError:
        limparTerminal()
        print('ERRO: Nome do arquivo inválido!')
    except IndexError:
        limparTerminal()
        print('ERRO: Digite um dos números abaixo!')
    except:
        limparTerminal()
        print('Ocorreu algum erro, tente novamente!')



