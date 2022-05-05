from random import randint
import time
import sys

pc = randint(0,5) #comando ppra gerar numero aleatótio
print('-=-' *20)
pensar = "Vou pensar em um número de 0 a 5. tente adivinhar.. \n"
for char in pensar:
          time.sleep(0.09)
          sys.stdout.write(char)
          sys.stdout.flush()
print('-=-' *20)
player = int(input('Em que número eu pensei?: '))
pro = "Processando.. \n"
time.sleep(0.5)
for char in pro:
          time.sleep(0.08)
          sys.stdout.write(char)
          sys.stdout.flush()
ganhou = "VOCÊ GANHOUUU!"
perdeu = "Você perdeu, eu pensei no número: {} e não no {}".format(pc,player)
time.sleep(2)
if player == pc:
    for char in ganhou:
          time.sleep(0.07)
          sys.stdout.write(char)
          sys.stdout.flush()
else:
    for char in perdeu:
          time.sleep(0.015)
          sys.stdout.write(char)
          sys.stdout.flush()
    
# for i in range(2):
#     a = input('VOcê é??')
#     if a == "sim":
#         print('aa gaayzao')
#     else:
#         print("ok")

# estiloso = str(input('Voce se considera estiloso(a)?'))
# estiloso.lower()
# if estiloso == "sim":
#     print("maath")
# else:
#     per = str(input("então você não é?"))
#     if per == "nao":
#         print('boa')
#     else:
#         print('saabia')

# # oi = str(input('pergunte oi'))
# # ola = str(input('ola'))
# # print(oi)
# # if oi == 'sim':
# #     print('ok')
# # else:
# #     m1 = str(input('Vc não ta bem?'))
# #     if m1 == 'sim':
# #         print('que bom')
# #     else:
# #         m2 = str(input('Porque?'))
