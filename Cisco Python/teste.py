import random

class NomeErro(TypeError):
    def __init__(self):
        TypeError.__init__(self)
        print('Digite um nome válido')

class ListErro(IndexError):
    def __init__(self):
        IndexError.__init__(self)
        print('Fila vazia!')

def EliminEspacos(texto):
    texto_mod = texto.split()
    return ''.join(texto_mod)

class Fila:
    def __init__(self):
        self.__ListaFila = []
        self.__lista_senhas = []

    def GerarSenha(self):
        __senha = random.randint(0, 999)
        if __senha in self.__lista_senhas:
            self.GerarSenha()
        else:
            self.__lista_senhas.append(__senha)
            return f'{__senha:0>3}'

    def AddFila(self, nome):
        if EliminEspacos(nome).isalpha():
            self.__ListaFila.append([nome, self.GerarSenha()])
            print(f'{nome} foi adicionado há fila')
        else:
            raise TypeError

    def Atender(self):
        if self.__ListaFila != []:
            nome, senha = self.__ListaFila.pop(0)
            print(f'''
=== Nome: {nome} ===
=== Senha: {senha} ===
''')
            return nome
        else:
            raise IndexError

    def getFila(self):
        mostra_fila = self.__ListaFila

        if mostra_fila != []:
            return mostra_fila
        else:
            raise IndexError

    def getLenFila(self):
        return len(self.__ListaFila)

def mostrarFila():
    fila = fila_unica.getFila()
    for x,cliente in enumerate(fila):
        nome, senha = cliente
        print(f'{x+1}. {nome}: {senha}', end=' | ')

def menu():
    print('''
====================
1. Adicionar a fila
2. Atender
3. Mostrar fila
0. Sair
''')
    return input('>>>: ')

if __name__ == '__main__':
    fila_unica = Fila()

    while True:
        try:
            resposta = menu()
            if resposta == '0':
                raise KeyboardInterrupt
                break
            elif resposta == '1':
                fila_unica.AddFila(input('Digite seu nome: '))
            elif resposta == '2':
                fila_unica.Atender()
                mostrarFila()
            elif resposta == '3':
                mostrarFila()
            else:
                print('Escolha uma das opções')
        except TypeError:
            NomeErro()
        except KeyboardInterrupt:
            print('Programa enerrado!')
            break
        except:
            ListErro()
