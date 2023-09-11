# Importar a biblioteca sqlite
import sqlite3

# Criando a conexão e o banco de dados
banco = sqlite3.connect('primeiro_banco.db')

# Criando o objeto cursor
cursor = banco.cursor()

# Criar nova tabela no banco
# cursor.execute("CREATE TABLE pessoa(id integer, nome text, idade integer, email text)")

# Inserir valores
cursor.execute("INSERT INTO pessoa VALUES(1, 'Maria', 38, 'maria@gmail.com')")

# Commit para enviar as informções para o banco de dados
banco.commit()

# Verificar o que foi adcionado
cursor.execute("SELECT * FROM pessoa")
print(cursor.fetchall())
