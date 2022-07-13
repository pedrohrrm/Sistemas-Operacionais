# Nomes: Enicarlos, Breno Thierry, Gustavo Vaz, Joao Paulo, Pedro Henrique Ribeiro

import threading
import time

#Cria o semaforo e passa como argumento quantas threadings poderao acessar o semaforo ao mesmo tempo.
semaphore = threading.Semaphore(1)

def funcao():
    # Adquire ao contador do semaforo em 1, logo ao executar a primeira função as outras não serão executadas por que nao tem mais espaços
    # Isso depende do tamanho do semaforo que foi definido la em cima, neste caso somente 1 threading pode acessar a função por vez.
    semaphore.acquire()
    print(semaphore)
    for i in range(1, 11):
        time.sleep(0.5)
        print(i)

    # Libera o semaforo, deixando a proxima threading acessar a função.
    semaphore.release()

# Cria as minhas threadings
funcao1 = threading.Thread(target=funcao)
funcao2 = threading.Thread(target=funcao)
funcao3 = threading.Thread(target=funcao)
funcao4 = threading.Thread(target=funcao)

# Inicia as threadings
funcao1.start()
funcao2.start()
funcao3.start()
funcao4.start()

#Print para mostrar que são trheadings executando, logo elas nao dependem da função principal.
print('Função principal finalizada.')
