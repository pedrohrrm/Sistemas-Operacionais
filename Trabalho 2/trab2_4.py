#Breno Thierry Barbalho Alencar
#Gustavo Vaz Fernandez
#Enicarlos Pereira Gonçaves junior
#João Paulo de Souza Costa
#Pedro Henrique Ribeiro Martins

import threading
import time

#impreção de 1 ao 10
def imprime():
    n = 1
    while (n <= 10):
      print("Sem uso Threads, imprime de  1 a 10 :", n)
      n = n + 1
      time.sleep(0.1)

def imprimeThread():
    n = 1
    while (n <= 10):
      print("Usando Threads, imprime de  1 a 10 :", n)
      n = n + 1
      time.sleep(0.1)

#Chamando as Funções
imprime()
print ("\n")
imprime = threading.Thread(target=imprime,args=()) #Instanciando uma Thread
imprimeThread = threading.Thread(target=imprimeThread,args=()) #Instanciando uma Thread

#Iniciando as Threads
imprime.start()
imprimeThread.start()