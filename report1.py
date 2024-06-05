import psycopg2
import sys
from collections import defaultdict

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
    param = args[0]
    query = f"""
    SELECT x, Xname, y, Yname, F, param1
    FROM T0
    WHERE param1 = '{param}'
    """
else:
    query = """
    SELECT x, Xname, y, Yname, F, param1
    FROM T0
    """

cursor.execute(query)
data = cursor.fetchall()

# Função para gerar o relatório
def generate_report(data):
    report = []
    current_x = None
    total_F = 0
    group_F = defaultdict(float)

    report.append(f"{'Report Title':^50}")
    report.append(f"{'='*50}")
    report.append(f"{'x':<10}{'y':<10}{'F':<10}")
    report.append(f"{'-'*50}")

    for row in data:
        x, Xname, y, Yname, F, param1 = row
        F = float(F)  # Converter Decimal para float
        if current_x != x:
            if current_x is not None:
                report.append(f"{'-'*50}")
                report.append(f"Total for {current_x}: {group_F[current_x]:<10.2f}")
                report.append(f"{'-'*50}")
            current_x = x
            report.append(f"{Xname:<10}")
        report.append(f"{'':<10}{Yname:<10}{F:<10.2f}")
        total_F += F
        group_F[current_x] += F

    report.append(f"{'-'*50}")
    report.append(f"Overall Total: {total_F:<10.2f}")
    return "\n".join(report)

# Imprimir o relatório no console
print(generate_report(data))

conn.close()
