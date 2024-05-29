import psycopg2

try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
        dbname="dbpython",
        user="postgres",
        password="An0025322",  # substitua "sua_senha" pela sua senha real
        host="localhost",
        port="5432"
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    def criar_tabela(conn, cur):
        cur.execute("""
        CREATE TABLE cliente (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(150)
        )
        """)
        conn.commit()

    def inserir_registro (conn, cur, nome, email):   
        data = (nome, email)
        cur.execute("INSERT INTO cliente(nome, email) VALUES (%s, %s);", data)
        conn.commit()
        
    def atualizar_registro(conn, cur, nome, email, id):
        data = (nome, email, id)
        cur.execute("UPDATE cliente SET nome = %s, email = %s WHERE id = %s", data) 
        conn.commit()
    def excluir_registro(conn, cur, id):
        data = (id,)
        cur.execute("DELETE FROM cliente WHERE id= %s", data)
        conn.commit()


    #atualizar_registro(conn, cur, "gui lessa","gui@gmail.com", 1)
    #inserir_registro(conn, cur, "André", "andre@gmail.com")
    #excluir_registro(conn, cur, 1)

    # Commit the transaction
    conn.commit()

    # No need to fetch for CREATE TABLE
    print("Tabela criada com sucesso")

except Exception as e:
    print(f"Erro ao conectar ou executar a query: {e}")

finally:
    # Close the cursor and connection to the database
    if cur:
        cur.close()
    if conn:
        conn.close()
