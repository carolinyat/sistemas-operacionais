import threading

# Variável compartilhada
contador = 0

# Semáforo para controlar o acesso à seção crítica
sem = threading.Semaphore()

# Função que simula uma seção crítica com controle
def secao_critica_com_controle():
    global contador
    for _ in range(1000000):
        sem.acquire()
        contador += 1
        sem.release()

# Cria 4 threads que acessam a seção crítica com controle
threads = []
for _ in range(4):
    t = threading.Thread(target=secao_critica_com_controle)
    threads.append(t)

# Inicia as threads
for t in threads:
    t.start()

# Aguarda até que todas as threads terminem
for t in threads:
    t.join()

# Imprime o valor final da variável compartilhada
print("Valor final da variável compartilhada (com controle):", contador)
