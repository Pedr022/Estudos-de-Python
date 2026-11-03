titulo = ['Nome', 'Pontos', 'Gols Marcados', 'Gols Sofridos', 'Saldo de Gols']

def AddTime():
    global titulo
    lista = []

    for e in range(4):
        valores = input(f'{titulo[e]}: ')
        if valores != '':
            lista.append(valores)
        else:
            raise ValueError

    saldo_gol = int(lista[2]) - int(lista[3])
    lista.append(saldo_gol)

    return lista

def MostrarTabela(tabela):
    global titulo

    print('\n', ' +'+('-'*104), end='+')
    print('\n', ' |', end='')
    
    for e in titulo:
        print(f'{e:<20}', end='|')
        
    print('\n', ' |'+('-'*104), end='|')
    
    for x, lin in enumerate(tabela):
        print(f'\n{x+1}.|', end='')
        for e in lin:
            print(f'{e:<20}', end='|')
            
    print('\n',' +'+('-'*104), end='+')

def Desempate(tabela):
    for x in range(len(tabela)-1):
        if int(tabela[x][1]) == int(tabela[x+1][1]):
                if int(tabela[x][4]) < int(tabela[x+1][4]):
                    temp = tabela[x]
                    tabela[x] = tabela[x+1]
                    tabela[x+1] = temp

    return MostrarTabela(tabela)

def OrdenarTabela(tabela):
    for e in range(len(tabela)):
        for i in range(len(tabela)-1):
            if int(tabela[i][1]) < int(tabela[i+1][1]):
                temp = tabela[i]
                tabela[i] = tabela[i+1]
                tabela[i+1] = temp

    return Desempate(tabela)

def Menu():
    print('''
=====================
1. Adicionar um time
2. Mostrar Tabela
0. Sair
''')
    return int(input('>>>: '))

if __name__ == '__main__':
    tabela_times = []

    while True:
        try:
            respostas = Menu()

            if respostas == 0:
                print('Programa encerrado!')
                break
            elif respostas == 1:
                tabela_times.append(AddTime())
            elif respostas == 2:
                if tabela_times[0] != None:
                    OrdenarTabela(tabela_times)
                    break
            else:
                print('ERRO: Selecione uma das opções acima!')
                
        except IndexError:
            print('ERRO: Nenhum time foi adicionado')
        except:
            print('ERRO: Valor inválido!')
            