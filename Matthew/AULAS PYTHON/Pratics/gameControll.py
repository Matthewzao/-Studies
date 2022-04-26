import pygame
from sys import exit
from random import randint

# INICIALIZANDO O PYGAME
pygame.init()

altura = 1000
largura = 900
tela = pygame.display.set_mode((altura,largura))                # DETERMINA O TAMANHO DA TELA
x = largura /2 # centralizando objeto
y = altura /2


pygame.display.set_caption("Matthew's Game")
relogio = pygame.time.Clock()                                   #ADICIONANDO UM FPS

while True:
    relogio.tick(60)                                            #CONTROLANDO O FPS   
    tela.fill((0,0,0))                                          #AQUI DETERMINA QUE A PARTE PRETA PREENCHA O RESTO DA TELA, PARA DAR O EFEITO DE ANIMAÇÃO
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                           #PARA O PROGRAMA FECHAR QUANDO CLICADO NO X
            pygame.quit()
            exit()       

            #CONTROLANDO O OBJETO

        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_a:                         
                x =x - 10
            if event.key == pygame.K_d:
                x =x + 10
            if event.key == pygame.K_w:
                y = y -10
            if event.key == pygame.K_s:
                y = y +10
            if event.key == pygame.K_z:
                x = x - 400
            if event.key == pygame.K_x:
                x = x +400

                #MEXER OBJETO COM TECLA PRESSIONADA
        if pygame.key.get_pressed()[pygame.K_a]:
            x = x -10
        if pygame.key.get_pressed()[pygame.K_d]:
            x = x +10
        if pygame.key.get_pressed()[pygame.K_s]:
            y = y +10
        if pygame.key.get_pressed()[pygame.K_w]:
            y = y -10

                #CONDIÇÃO DE COLISÃO
    retanguloVermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    retarnguloAzul = pygame.draw.rect(tela, (0,0,255), (200,300,40,50))

    if retanguloVermelho.colliderect(retarnguloAzul):
        print("colidiu")

    pygame.display.update()