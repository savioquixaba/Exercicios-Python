import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Conectando ao banco de dados PostgreSQL

connect = psycopg2.connect(
    dbname="meu_primeiro_banco",
    user="postgres",
    password="1122",
    host="localhost",
    port="5432"
)

# Lendo os dados da tabela

query = "SELECT data_venda, preco_unitario, quantidades FROM vendas"
df = pd.read_sql_query(query, connect)

# Fechando a conexão
connect.close()


pivot_df = df.pivot(index='data_venda', columns='preco_unitario', values='quantidades')

# Exibindo os dados pivoteados para verificar se foram lidos corretamente
print(pivot_df)

# Plotagem do histograma
pivot_df.plot(kind='bar', stacked="true")
plt.title('Quantidades Vendidas por Jogo ao Longo do Tempo')
plt.xlabel('Data da Venda')
plt.ylabel('Quantidade Vendida')
plt.grid(True)
plt.show()