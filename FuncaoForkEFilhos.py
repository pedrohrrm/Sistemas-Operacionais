##função fork e filhos

##a função fork é utilizada na criação de processos filhos
import os
import time

def filho(): ##função filho que vai imprimir Eu sou o filho e pegar o PID
    while(True):
        print("Eu sou o filho: PID {}. Meu pai é {} \n".format(os.getpid(),os.getppid()))
        time.sleep(5) ##tempo de espera para a execução de outra função

def pai():

    while(True):
##vai pegar o PID do processo pai
        print("Eu sou o Pai: PID {}. Meu Pai é {} \n".format(os.getpid(),os.getppid())) 
        time.sleep(5)

##início do programa

print("Executando o processo Pai – PID: {} \n".format(os.getpid()))

##cria o processo filho

retorno = os.fork() ##a partir daqui sera criado um processo filho, outro processo que irá ficar em outra área de memória.
##A partir desse ponto teremos processos pai e filho rodando
##temos então que definir qual código cada um irá rodar
##isso é feito através deste if obtido pela variável retorno
if retorno > 0: ## se o retorno for maior que zero vai executar o o código pai.
    pai()
else: ## se não for maior que zero vai executar o código filho.
    filho()