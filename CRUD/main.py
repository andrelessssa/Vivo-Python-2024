import psycopg2

# Conectar ao banco de dados
conexao = psycopg2.connect(
    host="localhost",
    database="crud_python",
    user="postgres",
    password="An0025322"
)

# Criar um cursor . vai executar os comendos
cursor = conexao.cursor()

# Crud Aqui
id_vendas = 1
nome_produto = "todynho"
valor = 6

comando = f"INSERT INTO vendas (id_vendas, nome_produto, valor) VALUES ({id_vendas}, '{nome_produto}', {valor})"


#cursor.execute(comando)
#conexao.commit() # editar o banco
#resultado = cursor.fetchall()  # ler o banco





# Fechar o cursor e a conexão
cursor.close()
conexao.close()
