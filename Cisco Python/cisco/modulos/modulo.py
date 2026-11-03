#!/Users/DRE SINOP 22/Documents/Nova pasta/cisco

#"" modulo.py - um exemplo de módulo em python ""

__counter = 0

def soma(lista):
    global __counter
    __counter += 1

    the_sum = 0

    for e in lista:
        the_sum += e

    return the_sum

def produto(lista):
    global __counter
    __counter += 1

    prod = 1

    for e in lista:
        prod *= e

    return prod

if __name__ == '__main__':
    print('eu prefiro feijão com farinha')

    minha_lista = list(range(1, 6))
    print(soma(minha_lista) == 15)
    print(produto(minha_lista) == 120)
