from Model import*

class Controlleradicionartarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
        try:
            if self.tarefa == '' or tarefa is int or tarefa is float:
                print("Não é possível adicionar uma tarefa vazia")
            else:
                if TODO.addTarefa(self.tarefa) == True:
                    print('Tarefa adicionada com sucesso')
                else:
                    print('Erro ao adicionar tarefa')

        except Exception as erro:
            print("Ta errado man.")
            return erro

class Controllerremovertarefa():
    def __init__(self, excluir):
        self.excluir = excluir
        try:
            if excluir is str or excluir is float:
                print("Não é possivel excluir a tarefa")

            else:
                if TODO.removeTarefa(self.excluir) == True:
                    print("Tarefa Excluida")

                else:
                    print("Algum problema foi encontrado")
        except Exception as erro:
            print("Ta errado man.")
            return erro
            

class Controllerlistartarefas():
    def __init__(self):
        controleLista = TODO.listaTarefas()
        cont = 1
        try:
            for i in controleLista:
                print(f'{cont}° - {i}')
                cont += 1
        except Exception as erro:
            print("Ta errado man.")
            return erro  