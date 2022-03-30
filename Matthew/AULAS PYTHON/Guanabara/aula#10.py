from re import T
import time
import sys

aprovado = "voce foi aprovado \n"
reprovado = "voce foi reprovado \n"

for i in range(10):
    n1 = float(input('digite uma nota: '))
    n2 = float(input('digite outra nota: '))
    m = (n1 + n2)/2
    print('=============')
    time.sleep(1)
    print('calculando Média...')
    time.sleep(1)
    print('Sua média foi {}'.format(m)) 
    print('=============')
    time.sleep(1)
    for e in range(3): 
        time.sleep(1)
        print('calculando resultado..')
        time.sleep(1)
    if m >= 6.0:
        for char in aprovado:
          time.sleep(0.05)
          sys.stdout.write(char)
          sys.stdout.flush() 
    else:
        for char in reprovado:
          time.sleep(0.05)
          sys.stdout.write(char)
          sys.stdout.flush() 
    print('Próximo Candidato..')