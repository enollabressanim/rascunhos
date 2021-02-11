'''
    referência: https://docs.python.org/3/library/sqlite3.html
'''
import sqlite3

# criar uma "conexão" com o banco de dados
conexao = sqlite3.connect("estoque.db")

# criar um curso para manipulação dos dados e tabelas
cursor = conexao.cursor()

# criar a tabela de produtos
cursor.execute('create table if not exists produto (id integer primary key,'\
    'nome text not null, quantidade real not null,'\
    'unidade text not null,'\
    'quantidade_minima real not null, localizacao text, fornecedores text,'\
    'data_ultima_compra text, preco_ultima_compra real,'\
    'descricao text)')

# fechar a conexão, tudo o que não tiver sobre um commit será perdido
conexao.close()
