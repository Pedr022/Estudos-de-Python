from sys import path
path.append('..\\modulos')

import modulo

zeros = [0 for i in range(5)]
ums = [1 for i in range(5)]

print(modulo.soma(zeros))
print(modulo.produto(ums))

