from Model import *

class Controlleradicionartarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def adicionar_tarefa(self):
        try:
            if self.tarefa == '' or isinstance(self.tarefa, (int, float)):
                raise ValueError("Não é possível adicionar uma tarefa vazia")
            
            if TODO.addTarefa(self.tarefa):
                print('Tarefa adicionada com sucesso')
            else:
                print('Erro ao adicionar tarefa')

        except Exception as erro:
            print("Ocorreu um erro: ", erro)

class Controllerremovertarefa():
    def __init__(self, excluir):
        self.excluir = excluir

    def remover_tarefa(self):
        try:
            if isinstance(self.excluir, (str, float)):
                raise ValueError("Não é possível excluir a tarefa")
            
            if TODO.removeTarefa(self.excluir):
                print("Tarefa Excluída")
            else:
                print("Algum problema foi encontrado")
        except Exception as erro:
            print("Ocorreu um erro: ", erro)

class Controllerlistartarefas():
    def listar_tarefas(self):
        try:
            controleLista = TODO.listaTarefas()
            cont = 1
            for i in controleLista:
                print(f'{cont}° - {i}')
                cont += 1
        except Exception as erro:
            print("Ocorreu um erro: ", erro)
