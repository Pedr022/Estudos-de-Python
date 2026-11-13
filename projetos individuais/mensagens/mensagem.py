import os
os.system('')

def escrever(texto):
    VERMELHO = '\033[31m'
    RESET = '\033[0m'
    return f'{VERMELHO}{texto}{RESET}'

if __name__ == '__main__':
    mensagem = ['_', '\\', '/']
    
    def linha1():
        print((' '+(escrever('_')*3)+' ')*2)
        print((escrever('/')+' '*3+escrever('\\'))*2)

    def linha2():
        print(('  '*e)+escrever('\\')+('  '*(4-(e*2)))+escrever('/'))
        print((' '+'  '*(e))+escrever('`')+('  '*(3-(e*2)))+escrever('´'))

    def ultimaLinha():
        fim = escrever('\\/')
        print((' '*4)+escrever('\\/')+(' '*4))

    linha1()

    for e in range(2):
        linha2()

    ultimaLinha()
