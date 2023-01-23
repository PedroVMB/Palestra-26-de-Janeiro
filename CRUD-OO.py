import mysql.connector

class Agenda:
    
    def connection(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root123',
            database = 'agenda'
        )
        self.cursor = self.conexao.cursor()
        
    
    def create(self, nome, telefone):
        comando = f'INSERT INTO contato (nome, telefone) VALUES ("{nome}", "{telefone}")'
        
        self.cursor.execute(comando)
        self.conexao.commit()
        
        self.cursor.close()
        self.conexao.close()
          
    def read(self):
        comando = 'SELECT * FROM contato'
        
        self.cursor.execute(comando)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)
        
        self.cursor.close()
        self.conexao.close()
        
    def update(self, id, nome, telefone):
        comando = f"UPDATE contato SET nome = '{nome}', telefone = '{telefone}' WHERE id = {id}"
        
        self.cursor.execute(comando)
        self.conexao.commit()
        
        self.cursor.close()
        self.conexao.close()

    def delete(self, id):
        comando = f"DELETE FROM contato WHERE id = '{id}'"
        
        self.cursor.execute(comando)
        self.conexao.commit()
        
        self.cursor.close()
        self.conexao.close()
    