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

# Função para gerar a tabela dinâmica
def generate_pivot_table(data):
    Xname_list = []
    Yname_list = []
    pivot_data = defaultdict(lambda: defaultdict(float))
    count_data = defaultdict(lambda: defaultdict(int))

    for row in data:
        x, Xname, y, Yname, F, param1 = row
        F = float(F)  # Converter Decimal para float
        if Xname not in Xname_list:
            Xname_list.append(Xname)
        if Yname not in Yname_list:
            Yname_list.append(Yname)
        pivot_data[Xname][Yname] += F
        count_data[Xname][Yname] += 1

    Xname_list.sort()
    Yname_list.sort()

    report = []
    report.append(f"{'Pivot Table Report':^50}")
    report.append(f"{'='*50}")
    header = f"{'':<10}" + "".join([f"{y:<10}" for y in Yname_list]) + f"{'Total':<10}"
    report.append(header)
    report.append(f"{'-'*50}")

    grand_total = 0
    for i, Xname in enumerate(Xname_list, 1):
        row = f"{i:<10}"
        row_total = 0
        for Yname in Yname_list:
            value = pivot_data[Xname][Yname]
            row += f"{value:<10.2f}"
            row_total += value
        grand_total += row_total
        row += f"{row_total:<10.2f}"
        report.append(row)

    report.append(f"{'-'*50}")
    footer = f"{'Total':<10}"
    for Yname in Yname_list:
        col_total = sum(pivot_data[Xname][Yname] for Xname in Xname_list)
        footer += f"{col_total:<10.2f}"
    footer += f"{grand_total:<10.2f}"
    report.append(footer)
    
    return "\n".join(report)

# Imprimir a tabela dinâmica no console
print(generate_pivot_table(data))

conn.close()
