
import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect("estoque.db")

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

produtos = []
for i in range(1,10):
    produtos.append( ("produto" + str(i), i + i/10.0, "unidade" + str(i),
        i/10.0) )

print("valores a serem inseridos: " + str(produtos))

# OBS: não utilize concatenação de string para montar a linha sql, seu 
# programa poderá ficar vulnerável a ataques de injeção de sql, ou seja,
# código sql maliciosos poderão ser inseridos no seu comando sql e realizar
# ações indesejadas
# Para evitar isso utilize substituição de parâmetros como no exemplo abaixo
cursor.executemany('insert into produto (id, nome, quantidade, unidade,'\
    'quantidade_minima) values (null, ?, ?, ?, ?)', produtos)

print("valores no banco de dados:")
for linha in cursor.execute("select * from produto"):
    print(linha)

# confirmar a operação
conexao.commit()

# fechar a conexão, tudo o que não tiver sobre um commit será perdido
conexao.close()
