from random import randint
import time


print("vou pensar em um numero, adivinhe!")
pc = randint(0,5)
ask = int(input("que numero eu pensei? "))
if ask == pc:
    print("você ganhou")
else:
    print("você perdeu, eu pensei no numero",pc,"e não no",ask)


