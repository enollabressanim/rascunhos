import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect('cadastro.db')

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

cursor.execute("DELETE from cliente WHERE nome = 'cliente 7'")

for linha in cursor.execute("select * from cliente"):
    print(linha)


# confirmar a operação
conexao.commit()

# fechar a conexão
conexao.close()