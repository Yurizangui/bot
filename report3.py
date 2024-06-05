import psycopg2
import matplotlib.pyplot as plt
import sys
from datetime import datetime

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    database="zangui",
    user="postgres",
    password="Zangui2012",
)

cur = conn.cursor()

# Receber os parâmetros T1 e T2 da linha de comando
if len(sys.argv) > 2:
    T1 = sys.argv[1]
    T2 = sys.argv[2]
else:
    T1 = None
    T2 = None

# Consultar os dados no intervalo [T1, T2]
if T1 and T2:
    query = """
        SELECT t, f1, f2
        FROM T0
        WHERE t BETWEEN %s AND %s
        ORDER BY t;
    """
    cur.execute(query, (T1, T2))
else:
    query = """
        SELECT t, f1, f2
        FROM T0
        ORDER BY t;
    """
    cur.execute(query)

data = cur.fetchall()

cur.close()
conn.close()

# Extrair dados das consultas
times = [row[0].strftime('%Y-%m-%d') for row in data]
f1_values = [row[1] for row in data]
f2_values = [row[2] for row in data]

# Plotar os dados
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Time')
ax1.set_ylabel('f1', color=color)
ax1.plot(times, f1_values, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('f2', color=color)
ax2.plot(times, f2_values, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title("f1(t) and f2(t) over Time")
plt.show()
