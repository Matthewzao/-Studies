from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
print('''YOUR CHOICES:
[0] STONE
[1] PAPER
[2] SCISSORS''')
player1 = int(input("Qual a Sua Jogada? "))
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")

print("-="*10)
pc = randint(0,2)
print("pc escolheu {}".format(itens[pc]))
print("jogador jogou {}".format(itens[player1]))
if pc == 0:
    if player1== 0:
        print("Empate!")
    elif player1 == 1:
        print("Você Ganhou!")
    elif player1 == 2:
        print("Você Perdeu!")
elif pc == 1:
    if player1 ==1:
        print("Empate!")
    elif player1 == 0:
        print("Você Perdeu!")
    elif player1 ==2:
        print("Você Ganhou!")
elif pc == 2:
    if player1 ==2:
        print("Empate!")
    elif player1 == 1:
        print("Você Perdeu!")
    elif player1 == 0:
        print("Você Ganhou!")

