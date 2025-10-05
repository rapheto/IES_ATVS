# 1 - Pesquise como implementar uma “Queue” na sua linguagem de programação preferida. Implemente um exemplo utilizando uma fila.
# 2 - Existe “Priority Queue” na sua linguagem de programação preferida? Pesquisee implemente …
# 3 - Agora defina 5 itens com alta prioridade, 5 com media e 5 com baixa e rode o algoritmo.O que foi possível observar?
# 4 - Implementar uma simulação de Round Robin:
# A) Cada processo possui: Um identificador (ex.: P1, P2, P3). Um tempo de execução total necessário (burst time – 5, 7 e 3, respectivamente).
# B) A fila deve conter os processos e ser manipulada apenas com Enqueue (inserir no fim) e Dequeue (remover do início).
# C) Cada processo deve executar no máximo por uma fatia de tempo (quantum definido como 2).
# D) Se ainda tiver tempo restante, deve ser enfileirado novamente. Se terminar, não retorna para a fila.
# E) A simulação deve imprimir a sequência de execução de cada processo até que todos sejam concluídosÇ

# Exemplo de saída Round Robin:
# P1 executou 2 unidades (restam 3)
# P2 executou 2 unidades (restam 5)
# P3 executou 2 unidades (restam 1)
# P1 executou 2 unidades (restam 1)
# P2 executou 2 unidades (restam 3)
# P3 executou 1 unidades (restam 0)
# P1 executou 1 unidades (restam 0)
# P2 executou 2 unidades (restam 1)
# P2 executou 1 unidades (restam 0)
# Todos os processos foram concluídos!

from queue import Queue
from queue import Queue, PriorityQueue

print("--- Parte 1: Exemplo de Fila Simples ---")
fila_simples = Queue()

print("Enfileirando: Tarefa A, Tarefa B, Tarefa C")
fila_simples.put("Tarefa A")
fila_simples.put("Tarefa B")
fila_simples.put("Tarefa C")

print("Processando a fila...")
while not fila_simples.empty():
    item = fila_simples.get()
    print(f"Executando -> {item}")
print("------Fila simples concluída!------\n")



print("--- Parte 2: Exemplo de Fila de Prioridade ---")
fila_de_prioridade = PriorityQueue()

print("Enfileirando itens com prioridades diferentes...")
fila_de_prioridade.put((2, "Tarefa Urgência Média"))
fila_de_prioridade.put((1, "Tarefa Urgência ALTA"))
fila_de_prioridade.put((3, "Tarefa Urgência Baixa"))

print("Processando a fila de prioridade...")
while not fila_de_prioridade.empty():
    prioridade, item = fila_de_prioridade.get()
    print(f"Executando -> {item} (Prioridade: {prioridade})")
print("------Fila de prioridade concluída!------\n")



print("--- Parte 3: Teste com 5 Itens de Cada Prioridade ---")
fila_teste = PriorityQueue()

print("Adicionando 15 tarefas com prioridades variadas...")
for i in range(1, 6):
    fila_teste.put((2, f"Média {i}"))   # Prioridade Média
    fila_teste.put((3, f"Baixa {i}"))   # Prioridade Baixa
    fila_teste.put((1, f"Alta {i}"))    # Prioridade Alta

print("\nProcessando a fila com múltiplas prioridades...")
while not fila_teste.empty():
    prioridade, item = fila_teste.get()
    print(f"Executando -> {item} (Prioridade: {prioridade})") 
print("Teste de múltiplas prioridades concluído!\n")
