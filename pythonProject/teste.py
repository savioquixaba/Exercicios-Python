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

# Lendo os dados da tabela e pivotando
query = "SELECT data_venda, name, quantidades FROM vendas"
df = pd.read_sql_query(query, connect)

pivot_df = df.pivot(index='data_venda',columns="name", values='quantidades')

# Fechando a conexão
connect.close()

# Exibindo os dados pivoteados para verificar se foram lidos corretamente
print(pivot_df)

ax = pivot_df.plot(kind='bar', stacked=True)

# Conjunto para rastrear nomes já adicionados
added_names = set()

# Adicionando os nomes dos jogos dentro das barras
for idx, column in enumerate(pivot_df.columns):
    for patch in ax.patches[idx::len(pivot_df.columns)]:
        # Verificando se o nome do jogo já foi adicionado
        if column not in added_names:
            # Obtendo a largura da barra
            width = patch.get_width()
            # Obtendo a altura da barra
            height = patch.get_height()
            # Adicionando o nome do jogo dentro da barra na vertical
            ax.text(patch.get_x() + width / 2, patch.get_y() + height / 2, column, ha='center', va='center', rotation=90)
            # Adicionando o nome do jogo ao conjunto de nomes adicionados
            added_names.add(column)

plt.title('Quantidades Vendidas por Jogo ao Longo do Tempo')
plt.xlabel('Data da Venda')
plt.ylabel('Quantidade Vendida')
plt.grid(True)
plt.show()