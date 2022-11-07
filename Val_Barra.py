import pandas as pd
import matplotlib.pyplot as plt
tabela = pd.read_excel(r"C:\Users\gabri\OneDrive\Área de Trabalho\BAGULHOS\FACULDADE\Periodo\Aula sexta\Prova\exames02.xlsx")

todos_servicos = tabela.groupby(['SERVIÇOS']).sum()
nome = ['EXAMES_DE_IMAGEM','EXAMES_DE_SANGUE','EXAMES_GERAIS']
val = todos_servicos["VALOR"]
jex = pd.DataFrame({"nomes": nome, "VAL": val})

plt.title('VALOR BRUTO (R$) NOS ULTIMOS 8 MESES ')
plt.bar(jex['nomes'],jex['VAL'], color="#228b22")

plt.grid(axis='y')
plt.show()