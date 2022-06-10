 ##PID E PPID
#importar a biblioteca
##PID é um idenficador que é atribuido pelo sistema operacional, esse identificador tem o nome de Process ID. (PID) O pid é o identifcado número que idenditica o processo dentro do SO. Cada Processo é associado a algum outro processo. Se é executado um programa encima desse Processo, o programa vai ter como Pai O processo anterior, nesse caso temos o identificador do pai do processo Parent Process ID. Se rodamos o navegador dentro do SO Linux, o identificador do pai do processo sera o identificador do Sheel do Linux. O pai do navegador sera o GNOME shell.
##com o programa iremos encontrar o PID e o PPID

import os

c

print("Obtendo PPID do Processo:")

print("PPID{}".format(os.getppid()))