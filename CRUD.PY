import mysql.connector



conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root123',
    database= 'bdyoutube'
)

cursor = conexao.cursor()

# CRUD



# CREATE 
nome_produto = "chocolate caro"
valor = 15

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() #CONEXAO PARA EDITAR O BANCO DE DADOS
resultado = cursor.fetchall() #Ler o banco de dados 


# READ


comando = 'SELECT * FROM vendas'
cursor.execute(comando)
conexao.commit() #CONEXAO PARA EDITAR O BANCO DE DADOS
resultado = cursor.fetchall() #Ler o banco de dados 
print(resultado)


# UPDATE


nome_produto = "Toddynho"
valor = 50

comando = F'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #CONEXAO PARA EDITAR O BANCO DE DADOS

# DELETE 

nome_produto = "Toddynho"
valor = 50

comando = F'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #CONEXAO PARA EDITAR O BANCO DE DADOS



cursor.close()
conexao.close()