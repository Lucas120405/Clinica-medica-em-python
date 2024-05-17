
class Paciente:
    def __init__(self, nome, data_nascimento):
        self._id = 1
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f'{self._id} - {self._nome} - {self._data_nascimento}'

    '''Setter alterar id do paciente'''
    def alterar_id_paciente(self, novo_id):
        self._id = novo_id

    '''Setter Alterar nome Paciente'''
    def alterar_nome_paciente(self, novo_nome):
        self._nome = novo_nome

    '''Setter alterar data de nascimento do paciente'''
    def alterar_data_nascimento_paciente(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento

    '''Getter mostrar id do paciente'''
    def mostrar_id_paciente(self):
        return self._id

    '''Getter mostrar nome do paciente'''
    def mostrar_nome_paciente(self):
        return self._nome

    '''Getter mostrar data de nascimento do paciente'''
    def mostrar_data(self):
        return self._data_nascimento