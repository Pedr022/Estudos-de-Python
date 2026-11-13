import time
from mensagem3 import escrever

def corrigeCaminho(caminho):
    nome = caminho.split('\\')
    return nome[-1]
    
def verifNomeArquivo(nome_arquivo):
    nome = str(corrigeCaminho(nome_arquivo)).split('.')

    try:
        if nome[-1] != 'txt':
            return False
        else:
            return True
    except IndexError:
        return False

def MenuCores():
    print('''
Escolha uma das cores abaixo:

+-----------------+
|   1. Branco     |
|   2. Preto      |
|   3. Vermelho   |
|   4. Verde      |
|   5. Amarelo    |
|   6. Magenta    |
+-----------------+
''')
    return input('>>> ')

def Menu():
    print('''
Escolha uma das opções abaixo:

1. Desenhar
2. Sair
''')
    return input('>>> ')

while True:
    opcao = Menu()

    if opcao == '2':
        print('Programa encerrado!')
        break
    elif opcao == '1':
        while True:
            nome_arquivo = input('Digite o caminho completo do arquivo: ')

            if verifNomeArquivo(nome_arquivo):
                arquivo = open(nome_arquivo, 'r')

                while True:
                    try:
                        cor = int(MenuCores()) - 1

                        for lin in arquivo.readlines():
                            for char  in lin:
                                if char == ' ':
                                    print(escrever(char, cor), end='', flush=True)
                                else:
                                    time.sleep(0.01)
                                    print(escrever(char, cor), end='', flush=True)
                        print('\n')

                        break
                    except:
                        print('ERRO: Valor de entrada inválido!')

                arquivo.close()
                break
            else:
                print('O arquivo precisa ser do tipo .txt')
    else:
        print('Escolha umas das opções acima!')
