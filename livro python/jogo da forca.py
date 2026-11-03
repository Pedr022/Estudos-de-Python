#jogo da forca
from random import randint
import time

nome_jogador = input('digite seu nome: ')

#palavras para sortear
#---------------------------------------------------------------------------------------------
entrada = open('palavras.txt', 'r')

lista_de_palavras = []
for linha in entrada.readlines():
    lista_de_palavras.append(linha)

entrada.close()
#---------------------------------------------------------------------------------------------

indice = randint(0, len(lista_de_palavras) - 1)

palavra = lista_de_palavras[indice].strip()
for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

linha1 = list('X  0  ')
linha2 = list('X     ')
linha3 = list('X     ')
linha4 = list('=' * (len(lista_de_palavras[indice]) - 1))

inicio = time.localtime()

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    print(''.join(linha4))

    if senha == palavra:
        fim = time.localtime()
        print('você acertou!\n')
        print(f'\ntempo: {fim.tm_hour - inicio.tm_hour}:{fim.tm_min - inicio.tm_min}:{fim.tm_sec - inicio.tm_sec}\n')
        break

    tentativa = input('\ndigite uma letra: ').lower().strip()

    if tentativa in digitadas:
        print('você ja tentou esta letra!')
        continue

    else:
        digitadas += tentativa

        if tentativa in palavra:
            acertos += tentativa

        else:
            erros += 1
            print('você errou!')

        print('X==:==\nX  :  ')
        print(''.join(linha1) if erros >= 1 else 'X')

        if erros == 2:
            linha2[3] = '|'

        elif erros == 3:
            linha2[2] = '\\'

        elif erros >= 4:
            linha2[4] = '/'

        print(''.join(linha2))

        if erros == 5:
            linha3[2] = '/'

        elif erros >= 6:
            linha3[4] = '\\'

        print(''.join(linha3))
        print('X\n===========')

        if erros == 6:
            fim = time.localtime()
            print('enforcado!')
            print(f'a palavra era: {palavra}')
            print(f'\ntempo: {fim.tm_hour - inicio.tm_hour}:{fim.tm_min - inicio.tm_min}:{fim.tm_sec - inicio.tm_sec}\n')
            break
