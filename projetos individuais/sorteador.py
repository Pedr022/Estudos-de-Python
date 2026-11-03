import random

def getQuantNums():
    return int(input('Quantidadede números disponíveis: '))

def getQuantApostas():
    return int(input('Quantidade de números que deseja jogar: '))

def sortear(qnt_apostas):
    global lista_numeros
    numero = random.randint(1,qnt_apostas)

    if numero in lista_numeros:
        return sortear(qnt_apostas)
    else:
        return lista_numeros.append(numero)

def escreverLista(lista):
    texto = sorted(lista)

    for e in texto:
        print(f'[{e}]', end=' ', flush=True)

    print('\n')

def Menu():
    print('''
1. sortear números
0. sair
''')
    return input('>>> ')

while True:
    try:
        lista_numeros = []
        menu = Menu()

        if menu == '0':
            print('>>>Programa encerrado<<<')
            break

        elif menu == '1':
            while True:
                numeros = getQuantNums()
                apostas = getQuantApostas()
                
                if numeros < apostas:
                    print('\n>>>número de apostas inválido<<<\n')
                    continue
                else:
                    for e in range(apostas):
                        sortear(numeros)

                    print('\n')
                    escreverLista(lista_numeros)
                    break
        else:
            print('>>>Escolha uma ds duas opções!<<<')

    except:
        print('ERRO: Ocorreu algo inesperado, tente novamente!')





        
