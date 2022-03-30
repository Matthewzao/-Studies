import time
import sys


print('-=-'*20) 

fab = "fabricio"

text = "adivinhe quem é \n"
for char in text:
        time.sleep(0.09)
        sys.stdout.write(char)
        sys.stdout.flush()

guess_who_is = str(input('qumem é quem é... faz mas não toma o cafe? '))
if guess_who_is == fab:
    yes = "yessir"
    for char in yes:
        time.sleep(0.09)
        sys.stdout.write(char)
        sys.stdout.flush()
else:
    nop = "aaaaaa não é"
    for char in nop:
        time.sleep(0.09)
        sys.stdout.write(char)
        sys.stdout.flush()


        