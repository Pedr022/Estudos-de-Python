import os

os.system('')
tempo1 = 0.1 
tempo2 = 0.03

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

def pintaChar(linha, cor=0):
    sleep(tempo1)
    for char in linha:
        if char == '.' or char == ' ':
            print(escrever(char, 1), end='', flush=True)
        else:
            sleep(tempo2)
            print(escrever(char, cor), end='', flush=True)

if __name__ == '__main__':
    from time import sleep
    import desenho as ds
    
    for key in ds.desenho2.keys():
        caractere = "'`-}=,"
        caractere2 = "#|_\\/"
        chaves = ['linha4', 'linha5', 'linha6', 'linha7']

        if key == 'linha7':
            pintaChar(ds.a1, 3)
            pintaChar(ds.a2, 4)

        elif key == 'linha11':
            pintaChar(ds.d1, 3)
            pintaChar(ds.d2)
            pintaChar(ds.d3, 3)

        elif key == 'linha12':
            pintaChar(ds.t1, 3)
            pintaChar(ds.t2, 5)
            pintaChar(ds.t3, 3)
            
        else:
            sleep(tempo1)
            for char in ds.desenho2[key]:
                if char == '.' or char == ' ':
                    print(escrever(char, 1), end='', flush=True)        
                    
                elif char in caractere2:
                    if key in chaves:
                        sleep(tempo2)
                        if char == '\\' or char == '/' or char == '|':
                            print(escrever(char, 4), end='', flush=True)
                        else:
                            print(escrever(char, 3), end='', flush=True)
                    else:
                        sleep(tempo2)
                        print(escrever(char, 3), end='', flush=True)
                elif char in caractere:
                    sleep(tempo2)
                    print(escrever(char, 4), end='', flush=True)
                else:
                    sleep(tempo2)
                    print(escrever(char), end='', flush=True)

        if key == 'linha13':
            pintaChar(ds.texto_msg, 2)
            
        print('\r')


