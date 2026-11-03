import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("C:\\Users\\DRE SINOP 22\\Downloads\\Cidadania Fiscal na Prática - Sinop.xlsx - Respostas ao formulário 1.csv")
print(tabela[tabela['Nome do Entrevistador'] == 'PEDRO HENRIQUE DE OLIVEIRA '])


#lendo dados de um arquivo ".csv"
# read_*
#titanic = pd.read_csv("C:\\Users\\DRE SINOP 22\\Downloads\\titanic.csv")

#print(titanic.head(8)) #primeiras linhas da tabela
#print(titanic.tail(10)) #ultimas linhas da tabelas
#print(titanic.dtypes) #tipo dos dados interpretados

#convertendo em excel
# instalar 'openpyxl'
# titanic.to_excel('titanic2.xlsx', sheet_name='passengers', index=False)

# resumo técnico de um DataFrame
#print(titanic.info())


#idade = titanic['Age']

#print(idade.head())
#print(type(idade))
#print(idade.shape)

#idade_sex = titanic[['Age', 'Sex']]

#print(idade_sex.head())
#print(type(idade_sex))
#print(idade_sex.shape)

# passageiros com mais de 35 anos
#above_35 = titanic[titanic['Age'] > 35]

#print(above_35.head())

#age_no_na = titanic[titanic['Age'].notna()]
#print(age_no_na)


#adult_names = titanic.loc[titanic['Age'] > 35, 'Name']
#print(adult_names)

#print(titanic.iloc[9:25, 2:5])
#titanic.iloc[0:3, 3] = 'anonimous'
#print(titanic.iloc[0:3, 3])


#air_quality = pd.read_csv("C:\\Users\\DRE SINOP 22\\Downloads\\air_quality_no2.csv", index_col=0, parse_dates=True)
#print(air_quality.plot())

#air_quality.plot.kde()

#air_quality.plot.area(x='station_london', y='station_paris', alpha=0.5)

#print([
#    method_name
#    for method_name in dir(air_quality.plot)
#    if not method_name.startswith('_')
#    ])

#asx = air_quality.plot.area(figsize=(12,4), subplots=True)

#fig, axs = plt.subplots(figsize=(12,4))

#air_quality.plot.area(ax=axs)
#axs.set_ylabel("NO$_2$ concentration")
#fig.savefig("no2_concentrations.png")

#print(plt.show())


#tabela = {
#    'X': [1,2,3,4,5,6,7,8,9,10],
#    'Ut': [12,22,30,36,40,42,42,40,36,32],
#    'Ume': [12,11,10,9,8,7,6,5,4,3.2],
#    'Uq': [0,10,8,6,4,2,0,-2,-4,-4]
#    }

#grafico = pd.DataFrame(tabela)

#grafico.plot.line(x='X', alpha=0.5)
#print(plt.show())

#Y1 = []

#x = -2
#for e in range(97):
#    eq1 = (1-(round(abs(x), 2)-1)**2)**0.5
#    Y1.append(eq1)
#    x += 1/24

#Y2 = []
#x = -2
#for e in range(97):
#    eq2 = (-2.5)*(1-(round(abs(x),2)/2)**0.5)**0.5
#    Y2.append(eq2)
#    x += 1/24

#X = []
#x = -2
#for e in range(97):
#    X.append(x)
#    x = float(f'{x+(1/24):.2f}')

#tabela = {'X': X,
#          'Y1': Y1,
#          'Y2': Y2}

#grafico = pd.DataFrame(tabela)
#print(grafico.info())

#grafico.plot.line(x='X', alpha=1)
#print(plt.show())
