import os
class ToDO():
    def __init__(self):
        self.lista = []

    def addTarefa(self, tarefa):
        self.lista.append(tarefa)
        return 1
        

    def removeTarefa(self, tarefa):
        self.lista.pop(tarefa)
        return 1

    def listarTarefa(self):
        arquivo = open('To-do.txt', 'r')
        arquivo.read()

def limpar():
    os.system('cls')

def parar():
    os.system('pause')