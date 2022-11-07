import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_excel(r"C:\Users\gabri\OneDrive\Área de Trabalho\BAGULHOS\FACULDADE\Periodo\Aula sexta\Prova\exames02.xlsx")
quant = pd.DataFrame(tabela['SERVIÇOS'].value_counts())

plt.title('EXAMES FEITOS NOS ULTIMOS 8 MESES')
plt.pie(quant['SERVIÇOS'], labels=quant.index, autopct="%1.1f%%",)
plt.legend(bbox_to_anchor=(1.5,1))

plt.show()