import pandas as pd

tabela = pd.read_csv("C:\\Users\\DRE SINOP 22\\Downloads\\Meteoros enviados.csv")
print(tabela.info())

print('\n')
verif_email = tabela[tabela['Campaign status.1'] == 'EMAIL_SENT']
print(verif_email)
print(verif_email.shape)

print('\n')

email = verif_email['EmailCompleto']

for e in email:
    teste = e.split('@')
    if teste[1] == 'edu.mt.gov.br':
        print(f'Um email foi enviado para {e}')
        print('\n')
        continue
    else:
        print(f'Email incorreto {e}')
        continue
