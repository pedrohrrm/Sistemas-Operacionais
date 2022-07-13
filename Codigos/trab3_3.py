""" 
Disciplina: Sistemas Operacionais
Trabalho 3: Problemas de sincronização de threads
Discentes: Igor Miranda,
           Renata Araújo,
           Walter Lopes,
           Wender Santos.
Docente: Alessandro Vivas 

"""

import time, threading

#objetos globais
TAM_LISTA = 10
mutex  = threading.Semaphore(1) #semáfaro 1
empty  = threading.Semaphore(TAM_LISTA)
full   = threading.Semaphore(0) #semafáro 2
lista = [TAM_LISTA] #definição do tamanho da lista
lista = list (range(0, TAM_LISTA)) #definindo o index da lista
cont_l  = 0 #contador dos leitores
cont_e  = 0 #contador dos escritores

def escrever(item):
   global lista, cont_e, empty, mutex
   empty.acquire()
   mutex.acquire()
   
   lista.append(item)
   if ((cont_e + 1) % TAM_LISTA == 0):
      cont_e = TAM_LISTA
   else: cont_e = (cont_e + 1) % TAM_LISTA
   
   mutex.release()
   full.release()

def ler():
   global lista, cont_l, full, mutex, cont_e
   full.acquire()
   mutex.acquire()
   
   item = lista[0]
   lista.remove(item)
   cont_l = (cont_l + 1) % TAM_LISTA
   if (cont_l == 0):
      cont_l = TAM_LISTA
      cont_e = 0
      
   mutex.release()
   empty.release()
   return item

def Escritor(item, command_parada):
   while True: 
      escrever(item)
      print (f'  Um escritor ecreveu: {item} Posição escrita: {cont_e}/{TAM_LISTA}')
      if command_parada():
         print("  Saindo da thread escritor.")
         break
      
def Leitor(command_parada):
   while True:
      time.sleep(0.5)
      item = ler()
      print (f'  Um leitor leu: {item} Posição lida: {cont_l}/{TAM_LISTA}')
      if command_parada():
            print("  Saindo da thread leitor.")
            break
      
      
#Programa principal
def main ():
   parar_threads = False
   container_threads = [] #lista de threads leitores e escritores
   print ('Escritores: ')
   for i in range (1,4):
      
      thread = threading.Thread(target=Escritor, args=(i,lambda: parar_threads))
      container_threads.append(thread) #enfileirando cada thread
      thread.start()
      
      thread = threading.Thread(target=Leitor, args=(lambda: parar_threads,))
      container_threads.append(thread) #enfileirando cada thread leitor criada 
      thread.start()
   time.sleep(3)
   
   print('\nEncerrando as threads.....\n')
   parar_threads = True
   for interator in container_threads:
        interator.join()
   
   print('\n')     
   print('\033[7;30;46m==========Programa finalizado.===========\033[m')
   print('\n')
   
if __name__ == '__main__':
    main()
   
