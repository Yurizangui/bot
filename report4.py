import psycopg2
import sys
import matplotlib.pyplot as plt

# Configuração da conexão
conn = psycopg2.connect(
    host='localhost',
    database="zangui",
    user="postgres",
    password="Zangui2012",
)
cursor = conn.cursor()

# Obter parâmetros da linha de comando
args = sys.argv[1:]

# Consultar o banco de dados
if args:
    param_y = args[0]
    query = f"""
    SELECT x, Xname, F
    FROM T0
    WHERE y = '{param_y}'
    """
else:
    query = """
    SELECT x, Xname, F
    FROM T0
    """

cursor.execute(query)
data = cursor.fetchall()

# Preparar dados para a diagramação
labels = [row[1] for row in data]
sizes = [float(row[2]) for row in data]  # Converter Decimal para float

# Plotar a diagramação
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

plt.title('Diagramação da Função A(F) por x')
plt.show()

conn.close()
