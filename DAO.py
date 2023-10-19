#Adiciona as tarefas ao arquivo.txt
def adicionar_tarefa(tarefa):
    with open('To-do.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()
        indice = len(tarefas) + 1
    with open('To-do.txt', 'a') as arquivo:
        arquivo.write(f"{indice} -- {tarefa}\n")


#Lista no terminal as tarefas do arquivo.txt
def listar_tarefas():
    with open('To-do.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()
        #Remove o ID da tarefa, aparecendo apenas o conteúdo
        for tarefa in tarefas:
            _, conteudo = tarefa.strip().split(" -- ", 1)
            print(conteudo)