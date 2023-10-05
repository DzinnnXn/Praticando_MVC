from Controller import*
import os

def parar():
    os.system('pause')

def limpar():
    os.system('cls')

while True:
    limpar()
    print('--|To-Do|--\n 1. Adicionar tarefa\n 2. Remover tarefa\n 3. Listar tarefas\n 0. Sair')
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            limpar()
            print("ADICIONAR TAREFA \n")
            tarefa = input('Digite a tarefa: ')
            addtarefa = Controlleradicionartarefa(tarefa)
            parar()

        case 2:
            limpar()
            print("REMOVER TAREFA \n")
            listartarefas = Controllerlistartarefas()
            excluir = int(input("Digite o indice da tarefa que deseja remover \n>>"))
            excluir -= 1
            excluirTarefa = Controllerremovertarefa(excluir)

        case 3:
            limpar()
            print("LISTAR TAREFAS \n")
            listartarefas = Controllerlistartarefas()
            parar()
                    
        case 0:
            break
        
        case _:
            print('Opção inválida')
            parar()