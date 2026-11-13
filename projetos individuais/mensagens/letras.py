import time

letras = {'10': ' \n \n \n',
          '32': '   \n   \n   ',
          '44': '   \n   \n,  ',
          '45': '   \n__ \n   ',
          '46': '   \n   \n.  ',
          '58': '   \n.  \n.  ',
          '65': '     \n /\\  \n/--\\ ',
          '66': ' __  \n|__) \n|__) ',
          '67': ' __ \n|   \n|__ ',
          '68': ' __  \n|  \\ \n|__/ ',
          '69': ' __ \n|__ \n|__ ',
          '70': ' __ \n|__ \n|   ',
          '71': ' __  \n| _  \n|__| ',
          '72': '     \n|__| \n|  | ',
          '73': '. \n| \n| ',
          '74': '  _ \n  | \n|_| ',
          '75': '   \n|/ \n|\\ ',
          '76': '   \n|  \n|_ ',
          '77': '     \n|\\/| \n|  | ',
          '78': '     \n|\\ | \n| \\| ',
          '79': ' __  \n|  | \n|__| ',
          '80': ' _  \n|_| \n|   ',
          '81': ' __  \n|  | \n|_\\| ',
          '82': ' _  \n|_| \n| \\ ',
          '83': ' __  \n|__  \n __| ',
          '84': '___ \n |  \n |  ',
          '85': '     \n|  | \n|__| ',
          '86': '     \n\\  / \n \\/  ',
          '87': '     \n|  | \n|/\\| ',
          '88': '   \n\\/ \n/\\ ',
          '89': '   \n\\/ \n/  ',
          '90': '_  \n / \n/_ ',
          '193': '  /  \n /\\  \n/--\\ ',
          '195': ' ~~  \n /\\  \n/--\\ ',
          '199': ' __ \n|__ \n /  ',
          '201': ' __/\n|__ \n|__ ',
          '202': ' __^\n|__ \n|__ ',
          '211': ' __/ \n|  | \n|__| ',
          '213': ' __~ \n|  | \n|__| ',
          '218': '  /  \n|  | \n|__| '}

lista_letras = []

def escrever(lista):
    time.sleep(1.5)
    for e in range(3):
        for i in range(len(lista)):
            if lista[i][e] == '':
                print(' ', end='', flush=True)
                continue
            print(lista[i][e], end='', flush=True)

        print('')

def transformList(palavra):
    global lista_letras
    global letras
    lista_letras = []
    for e in palavra.upper():
        letra = str(ord(e))
        if letra == '10':
            print('\n')
            break
        lista_letras.append(letras[letra].split('\n'))

arquivo1 = open('texto.txt', 'r', encoding='utf-8')

for e in arquivo1.readlines():
    transformList(e)
    escrever(lista_letras)

transformList('ass: pedro h.')
escrever(lista_letras)

arquivo1.close()



        
