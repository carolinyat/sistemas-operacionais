import threading

# Variável compartilhada
contador = 0

# Função que simula uma seção crítica sem controle
def secao_critica_sem_controle():
    global contador
    for _ in range(1000000):
        contador += 1

# Cria 4 threads que acessam a seção crítica sem controle
threads = []
for _ in range(4):
    t = threading.Thread(target=secao_critica_sem_controle)
    threads.append(t)

# Inicia as threads
for t in threads:
    t.start()

# Aguarda até que todas as threads terminem
for t in threads:
    t.join()

# Imprime o valor final da variável compartilhada
print("Valor final da variável compartilhada (sem controle):", contador)
