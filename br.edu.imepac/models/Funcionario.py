class Funcionarios:
    def __init__(self, id, nome, cargo):
        self._id = id
        self._nome = nome
        self._cargo = cargo

    def __str__(self):
        return f'{self._id} - {self._nome} - {self._cargo}'

    '''Setter Alterar id'''
    def alterar_id_funcionario(self, novoid):
        self._id = novoid

    '''Setter Alterar Nome'''
    def alterar_nome_funcionario(self, novonome):
        self._nome = novonome

    '''Setter Alterar Cargo'''
    def alterar_cargo_funcionario(self, novocargo):
        self._nome = novocargo

    '''Getter mostrar id'''
    def mostrar_id_funcionario(self):
        return self._id

    '''Getter mostrar nome'''
    def mostrar_nome_funcionario(self):
        return self._nome

    '''Getter mostrar cargo'''
    def mostrar_cargo_funcionario(self):
        return self._cargo