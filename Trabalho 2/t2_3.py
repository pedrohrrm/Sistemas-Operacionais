#Breno Thierry Barbalho Alencar
#Gustavo Vaz Fernandes
#Enicarlos Pereira Gonçalves Junior
#João Paulo de Souza Costa
#Pedro Henrique Ribeiro Martins

import os, sys

print ('a filho escreve o texto ')
print ('o pai vai ler o texto escrito pela filho...')

# Descritores de arquivos; r,w para leitura e escrita
r, w = os.pipe() 

processid = os.fork()
if processid:
    # Processo pai
    # Fecha o descritor de arquivo w
    os.close(w)
    r = os.fdopen(r)
    str = r.read()
    print ('o pai le')
    
    print ('texto =', str )  
    sys.exit(0)
else:
    # Este é o processo filho
    os.close(r)
    w = os.fdopen(w, 'w')
    print ('a filho escrevendo')
    w.write("o texto escrito pela criança...")
    w.close()
    print ('a filho termina')
    sys.exit(0)