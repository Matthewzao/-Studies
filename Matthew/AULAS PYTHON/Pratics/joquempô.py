from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''YOUR CHOICES:
[0] STONE
[1] PAPER
[2] SCISSORS''')
player1 = int(input("whats your play? "))
print("-="*10)
print("pc escolheu {}".format(itens[pc]))
print("jogador jogou {}".format(itens[player1]))
print("-="*10)

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
