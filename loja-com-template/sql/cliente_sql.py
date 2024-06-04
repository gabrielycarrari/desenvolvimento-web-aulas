SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        data_nascimento DATE NOT NULL,
        endereco TEXT NOT NULL
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        telefone TEXT NOT NULL,
        admin BOOLEAN NOT NULL,
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO produto(nome, cpf, data_nascimento, endereco, email, senha, telefone, admin)
    VALUES (?, ?, ?, ?, ?, ?, ?. ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, cpf, data_nascimento, endereco, email, telefone, admin
    FROM cliente
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE cliente
    SET nome=?, cpf=?, data_nascimento=?, endereco=?, email=?, telefone=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM cliente
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome, cpf, data_nascimento, endereco, email, telefone, admin
    FROM cliente
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM cliente
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome, cpf, data_nascimento, endereco, email, telefone, admin
    FROM cliente
    WHERE nome LIKE ? OR cpf LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM cliente
    WHERE nome LIKE ? OR cpf LIKE ?
"""