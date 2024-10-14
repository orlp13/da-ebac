
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados do arquivo CSV
df_gasolina = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df_gasolina)
plt.title('Preço Médio da Gasolina em São Paulo (Julho/2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.savefig('gasolina.png')
plt.show()
    