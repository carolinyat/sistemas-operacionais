import threading # módulo threading, que permite trabalhar com threads em Python
import time # módulo time, que fornece funcionalidades relacionadas ao tempo
import random # módulo random, usado para gerar números aleatórios

# Função que simula o processamento de um pedido
def processar_pedido(numero_pedido):
    print(f"Processando pedido {numero_pedido}")
    tempo_processamento = random.randint(1, 5) # tempo de processamento aleatório entre 1s a 5s
    time.sleep(tempo_processamento) # simulação do tempo de processamento
    print(f"Pedido {numero_pedido} pronto em {tempo_processamento} segundos")

# Número de pedidos a serem processados
numero_pedidos = 5

# Cria uma lista de threads
threads = []

# Cria e inicia as threads
for i in range(numero_pedidos):
    thread = threading.Thread(target=processar_pedido, args=(i+1,))
    threads.append(thread) # adiciona a lista de threads
    thread.start() # inicia a thread

# Espera todas as threads terminarem
for thread in threads:
    thread.join() # aguardar que uma thread específica termine sua execução antes de continuar a execução do programa principal

print("Todos os pedidos foram processados!")
