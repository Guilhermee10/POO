class Lista:
    def __init__(self):
        self.tarefas = []
        self.importancia = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'Sua tarefa "{tarefa}" foi adicionada à lista!')
        print(self.tarefas)

    def remover_item(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            print(f'A tarefa "{tarefa}" foi removida.')
        else:
            print('Tarefa não encontrada!')
        print('Sua lista ficou assim:', self.tarefas)

    def adicionar_importancia(self, importancia_tarefa):
        self.importancia.append(importancia_tarefa)
        print('Lista de tarefas:', self.tarefas)
        print('Importâncias:', self.importancia)


# Exemplo de uso
lista = Lista()

nome_tarefa = input('Qual tarefa deseja adicionar?: ')
lista.adicionar_tarefa(nome_tarefa)

importancia = input('Escolha a importância da sua tarefa!: ')
lista.adicionar_importancia(importancia)

tarefa_remover = input('Qual tarefa deseja remover?: ')
lista.remover_item(tarefa_remover)
