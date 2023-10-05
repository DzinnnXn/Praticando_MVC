class ToDo():
    def __init__(self):
        self.lista = []

    def addTarefa(self, tarefa):
        self.lista.append(tarefa)
        return True

    def removeTarefa(self, excluir):
        self.lista.pop(excluir)
        return True

    def listaTarefas(self):
        return self.lista

TODO = ToDo()