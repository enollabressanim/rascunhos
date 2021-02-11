# 05_create_data_param.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# solicitando os dados ao usuário
p_nome = input('Nome: ')
p_CPF = input('CPF: ')
p_RG = input('RG: ')
p_telefone = input('telefone: ')
p_celular = input('celular: ')
p_email = input('email: ')
p_rua = input('rua: ')
p_numero = input('numero: ')
p_bairro = input('bairro: ')
p_cidade = input('cidade: ')
p_estado = input('estado: ')
p_CEP = input('CEP: ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", (p_nome, p_CPF, p_RG, p_telefone, p_celular, p_email, p_rua, p_numero, 
      p_bairro, p_cidade, p_estado, p_CEP))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()