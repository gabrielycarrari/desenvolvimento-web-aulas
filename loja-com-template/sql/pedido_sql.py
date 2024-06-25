SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora DATETIME NOT NULL,
        valor_total FLOAT NOT NULL,
        endereco_entrega TEXT NOT NULL,
        estado INTEGER NOT NULL,
        id_cliente INTEGER,
        FOREIGN KEY id_cliente REFERENCES cliente(id))
"""

SQL_INSERIR = """
    INSERT INTO pedido(data_hora, valor_total, endereco_entrega, estado, id_cliente)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_ALTERAR_ESTADO = """
    UPDATE pedido
    SET estado=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM pedido
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, data_hora, valor_total, endereco_entrega, estado
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM pedido
    WHERE id_cliente=?
"""

SQL_OBTER_POR_PERIODO = """
    SELECT id, data_hora, valor_total, endereco_entrega, estado, id_cliente, cliente.nome AS nome_cliente
    FROM pedido LEFT JOIN cliente ON id_cliente = cliente.id
    WHERE (id_cliente = ?) AND (data_hora BETWEEN ? AND ?)
    ORDER BY data_hora DESC
"""

SQL_OBTER_QUANTIDADE_PERIODO = """
    SELECT COUNT(*) FROM pedido
    WHERE (id_cliente = ?) AND (data_hora BETWEEN ? AND ?)
"""
