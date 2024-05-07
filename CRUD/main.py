import psycopg2

# Conectar ao banco de dados
conexao = psycopg2.connect(
    host="localhost",
    database="crud_python",
    user="postgres",
    password="An0025322"
)

# Criar um cursor
cursor = conexao.cursor()

# Executar comandos SQL
cursor.execute("select * from vendas")
registros = cursor.fetchall()

# Exemplo: imprimir registros
for registro in registros:
    print(registro)

# Fechar o cursor e a conexão
cursor.close()
conexao.close()

