import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_excel(r"C:\Users\gabri\OneDrive\Área de Trabalho\BAGULHOS\FACULDADE\Periodo\Aula sexta\Prova\exames02.xlsx")

exImg = tabela["SERVIÇOS"] == "EXAMES_DE_IMAGEM"
te = tabela[exImg]
quant = pd.DataFrame(te['ATENDIMENTOS'].value_counts())
top = quant.head(10)

top.plot.barh( fontsize=6, color='#052498' ,title='Quantidade de “exames de imagem(por tipo)”em 8 meses')

plt.show()