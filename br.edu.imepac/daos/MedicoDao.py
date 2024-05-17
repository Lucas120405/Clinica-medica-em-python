import ConnectionFactory

banco = ConnectionFactory.conectarbanco('localhost', 'root', '', 'clinicamedica')

cursor = banco.cursor()
