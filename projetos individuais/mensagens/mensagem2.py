import time
from desenho import desenho

for key in desenho.keys():
    time.sleep(0.1)
    for char in desenho[key]:
        if char == ' ':
            print(char, end='', flush=True)
        else:
            time.sleep(0.05)
            print(char, end='', flush=True)
    print('\r')
