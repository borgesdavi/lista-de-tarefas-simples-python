"""
Feito por: Davi Borges (2025)
Repositório: https://github.com/borgesdavi

🗒️ Descrição:
Lista de tarefas simples desenvolvida em Python

🎯 Objetivo:
Praticar a manipulação de listas em Python

🛠️ Versão: 1.0
"""

lista_de_tarefas = []


def ver_tarefas():
    if not lista_de_tarefas:
        print('A lista de tarefas está vazia!')
    else:
        for i, tarefa in enumerate(lista_de_tarefas):
            print(f'{i + 1}) {tarefa}')


def adicionar_tarefa():
    tarefa = input('Tarefa: ')
    lista_de_tarefas.append(tarefa)
    print(f'Tarefa {tarefa} adicionada com sucesso!')


def remover_tarefa():
    if not lista_de_tarefas:
        print('A lista de tarefas está vazia!')
    else:
        ver_tarefas()
        tarefa = int(
            input('Digite o índice da tarefa que você deseja remover: ')) - 1
        if 0 <= tarefa < len(lista_de_tarefas):
            tarefa_removida = lista_de_tarefas.pop(tarefa)
            print(f'Tarefa {tarefa_removida} removida com sucesso!')
        else:
            print('Tarefa inválida!')


def menu():
    while True:
        print('[1] Ver tarefas')
        print('[2] Adicionar tarefa')
        print('[3] Remover tarefa')
        print('[0] Sair')

        opcao = int(input('Digite uma opção: '))

        match opcao:
            case 1:
                ver_tarefas()
            case 2:
                adicionar_tarefa()
            case 3:
                remover_tarefa()
            case 0:
                break
            case _:
                print('Opção inválida!')


menu()
