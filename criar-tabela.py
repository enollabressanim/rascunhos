# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        CPF VARCHAR(11) NOT NULL,
        RG VARCHAR(7) NOT NULL,
        telefone VARCHAR(10),
        celular VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        rua TEXT,
        numero TEXT,
        bairro TEXT,
        cidade TEXT,
        estado TEXT,
        CEP VARCHAR(8) NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()