#Breno Thierry Barbalho Alencar
#Gustavo Vaz Fernandes
#Enicarlos Pereira Gonçalves Junior
#João Paulo de Souza Costa
#Pedro Henrique Ribeiro Martins


#a função fork vai ser utilizada na criação de processos filhos
import os
import time

def pai():
    while(True):
#vai usar imprimir Pai e o PID e PPID do processo pai
        print("Pai: PID {}, PPID {} \n".format(os.getpid(),os.getppid())) 
        time.sleep(10)
def filho(): #vai imprimir Filho e o PID e PPID.
    while(True):
        print("Filho: PID {}, PPID {} \n".format(os.getpid(),os.getppid()))
        time.sleep(10) #tempo de espera para a execução de outra função, se retirar vai executar direto sem intervalo.

#início do programa

print("Executando o processo Pai – PID: {} \n".format(os.getpid()))

#criação do processo filho

retorno = os.fork() #A partir dessa linha vamos criar o processo filho, assim, outro processo vai ficar em outra área de memória.
#Então, teremos teremos processos pai e filho executando
#será necessário definir qual código cada um irá rodar isso é feito através do if obtido pela variável retorno
if retorno > 0: # se o retorno for maior que zero vai realizar a execução do código pai.
    pai()
else: #se não, vai realizar a execução do código filho.
    filho()