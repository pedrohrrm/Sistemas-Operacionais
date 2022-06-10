#Breno Thierry Barbalho Alencar
#Gustavo Vaz Fernandes
#Enicarlos Pereira Gonçalves Junior
#João Paulo de Souza Costa
#Pedro Henrique Ribeiro Martins

#importar a bibilioteca os
import os

#imprimindo o PID do processo
print("Valor do PID do processo em execução é:")
print("{}".format(os.getpid()))

#imprimindo o PPID do processo
print("Valor do PPID do processo em execução é:")
print("{}".format(os.getppid()))