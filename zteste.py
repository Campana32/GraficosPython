import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_excel(r"C:\Users\gabri\OneDrive\Área de Trabalho\BAGULHOS\FACULDADE\Periodo\Aula sexta\Prova\exames02.xlsx")

# VERSÃO MAIS SIMPLES
# plt.title('EXAMES FEITOS NOS ULTIMOS 8 MESES')
# plt.hist(tabela['SERVIÇOS'])

nome = ['EXAMES_DE_IMAGEM','EXAMES_DE_SANGUE','EXAMES_GERAIS']
exval = tabela['SERVIÇOS'].value_counts()
jex = pd.DataFrame({"nomes": nome, "EXVAL": exval})
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

ax1.set_xlabel('Tipos', fontsize = 12)
ax1.set_ylabel('Quantidade', fontsize = 12)

ax1.set_title('EXAMES FEITOS NOS ULTIMOS 8 MESES', fontsize = 16)

plt.bar(jex['nomes'],jex['EXVAL'], color=['blue', 'red', 'green'])

plt.show()