import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_excel(r"C:\Users\gabri\OneDrive\Área de Trabalho\BAGULHOS\FACULDADE\Periodo\Aula sexta\Prova\exames02.xlsx")

nome = ['EXAMES_DE_IMAGEM','EXAMES_DE_SANGUE','EXAMES_GERAIS']
exval = tabela['SERVIÇOS'].value_counts()
jex = pd.DataFrame({"nomes": nome, "EXVAL": exval})
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)

ax1.set_xlabel('Tipos', fontsize = 14)
ax1.set_ylabel('Quantidade', fontsize = 14)

ax1.set_title('EXAMES FEITOS NOS ULTIMOS 8 MESES', fontsize = 16)

plt.bar(jex['nomes'],jex['EXVAL'], color=['#6f00ff', '#864ee2', '#3d1577'])

plt.show()
