# x = float(input('Digite o valor para x: '))
# y = 1/(x+(1/(x+(1/(x+(1/x))))))
# print(f'y = {y}')

x = float(input('Digite o valor para x: '))
y = 1/x

iterador = 0
while iterador <= 2:
    y = 1/(x + (y))
    iterador += 1

print(f'y = {y}')