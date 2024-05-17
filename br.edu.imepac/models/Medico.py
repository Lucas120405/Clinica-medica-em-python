class Medico:
    def __init__(self, nome, crm, especialidade):
        self._id = 1
        self._nome = nome
        self._crm = crm
        self._especialidade = especialidade

    def __str__(self):
        return f'{self._id} - {self._nome} - {self._crm} - {self._especialidade}'

    '''Setter Alterar id'''
    def alterar_id_medico(self, novoid):
        self._id = novoid

    '''Setter Alterar Nome'''
    def alterar_nome_medico(self, nome):
        self._nome = nome

    '''Setter Alterar Crm'''
    def alterar_crm_medico(self, crm):
        self._nome = crm

    '''Setter Alterar Especialidade'''
    def alterar_especialidade_medico(self, especialidade):
        self._especialidade = especialidade

    '''Getter mostrar id'''
    def mostrar_id_medico(self):
        return self._id

    '''Getter mostrar nome'''
    def mostrar_nome_medico(self):
        return self._nome

    '''Getter mostrar crm'''
    def mostrar_crm_medico(self):
        return self._crm

    '''Getter mostrar especialidade'''
    def mostrar_especialidade_medico(self):
        return self._especialidade
