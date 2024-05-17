import mysql.connector

'''#Conexão com o Banco:'''


def conectarbanco(host, user, password, database):
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conexao


