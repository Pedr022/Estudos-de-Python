agenda = []

def pede_nome():
    return input('nome: ')

def pede_telefone():
    return input('telefone: ')

def mostra_dados(nome, telefone):
    print(f'nome: {nome} telefone: {telefone}')

def pede_nome_arquivo():
    return input('nome do arquivo: ')

def pesquisa(nome):
    mnome = nome.lower()

    for p, e in enumerate(agenda):
        if  e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)

    if p != None:
        del agenda[p]

    else:
        print('nome não encontrado')

def altera():
    p = pesquisa(pede_nome())

    if p != None:
        nome = agenda[p][0]
        telefone = agenda[p][1]

        print('encontrado:')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]

    else:
        print('nome não encontrado')

def lista():
    print('\nagenda\n\n------')

    for e in agenda:
        mostra_dados(e[0], e[1])

    print('------')

def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, 'r')
    agenda = []

    for l in arquivo.readlines():
        nome = l.strip().split('#')
        telefone = l.strip().split('#')
        agenda.append([nome, telefone])

    arquivo.close()

def grava():
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, 'w')

    for e in agenda:
        arquivo.write(f'{e[0]}#{e[1]}\n')

    arquivo.close()

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))

            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print(f'valor invalido, por favor digitar entre {inicio} e {fim}')

def menu():
    print('''
    1 - novo
    2 - altera
    3 - apaga
    4 - lista
    5 - grava
    6 - lê

    0 - sai
''')
    return valida_faixa_inteiro('escolha uma opção: ', 0, 6)

while True:
    opcao = menu()

    if opcao == 0:
        break

    elif opcao == 1:
        novo()

    elif opcao == 2:
        altera()

    elif opcao == 3:
        apaga()

    elif opcao == 4:
        lista()

    elif opcao == 5:
        grava()

    elif opcao == 6:
        le()
