
from sre_parse import State
import pygame
from sys import exit
from random import randint

# INICIALIZANDO O PYGAME
pygame.init()

# Inserindo e tocando musica
colisaoSong = pygame.mixer.Sound('smw_coin.wav')

altura = 1000
largura = 900
tela = pygame.display.set_mode((altura,largura))                # DETERMINA O TAMANHO DA TELA
x = largura /2 # centralizando objeto
y = altura /2
b = largura /2
a = altura /2

pontos = 0
pontos2 = 0


fonte = pygame.font.SysFont('papyrus',20,True, True)
fonte2 = pygame.font.SysFont('papyrus',20,True, True)
x_azul = randint(40,700)
y_azul = randint(50,430)
b_azul = randint(40,700)
a_azul = randint(50,430)
pygame.display.set_caption("Matthew's Game")
relogio = pygame.time.Clock()                                   #ADICIONANDO UM FPS
pause = False

while True:
    relogio.tick(60)                                            #CONTROLANDO O FPS   
    tela.fill((18,20,20))                                          #AQUI DETERMINA QUE A PARTE PRETA PREENCHA O RESTO DA TELA, PARA DAR O EFEITO DE ANIMAÇÃO
    mensagem = f'Pontos: {pontos}'                              
    mensagem2 = f'Pontos: {pontos2}'
    textoFormatado = fonte.render(mensagem, False,(200,0,0))
    textoFormatado2 = fonte2.render(mensagem2, True,(250,100,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:                           #PARA O PROGRAMA FECHAR QUANDO CLICADO NO X
            pygame.quit()
            exit()       

            #CONTROLANDO O OBJETO

        # if event.type == pygame.KEYDOWN:    
        #     if event.key == pygame.K_a:                         
        #         x =x - 10
        #     if event.key == pygame.K_d:
        #         x =x + 10
        #     if event.key == pygame.K_w:
        #         y = y -10
        #     if event.key == pygame.K_s:
        #         y = y +10
        #     if event.key == pygame.K_z:
        #         x = x - 400
        #     if event.key == pygame.K_x:
        #         x = x +400

            #MEXER OBJETO COM TECLA PRESSIONADA

# PLAYER1
    if pygame.key.get_pressed()[pygame.K_a]:
        x = x -5   
    if pygame.key.get_pressed()[pygame.K_d]:
        x = x +5
    if pygame.key.get_pressed()[pygame.K_s]:
        y = y +5
    if pygame.key.get_pressed()[pygame.K_w]:
        y = y -5
                # PLAYER2
    if pygame.key.get_pressed()[pygame.K_UP]:
        a = a -5   
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        a = a +5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        b = b +5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        b = b -5


 #CONDIÇÃO DE COLISÃO                            COR            TAMANHO
    retanguloVermelho = pygame.draw.rect(tela, (200,0,0), (x,y,25,25))
    retanguloPlayer2 = pygame.draw.rect(tela, (250,100,200), (b,a,25,25))

    retarnguloAzul = pygame.draw.rect(tela, (0,255,255), (x_azul,y_azul,6,6))
    retarnguloBranco = pygame.draw.rect(tela, (0,255,222), (b_azul,a_azul,6,6))

    if retanguloVermelho.colliderect(retarnguloAzul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos +1
        colisaoSong.play()
        if pontos == 10:
            break
            
            
    if retanguloPlayer2.colliderect(retarnguloBranco):
        b_azul = randint(40,700)d
        a_azul = randint(50,430)
        pontos2 = pontos2 +1
        colisaoSong.play()
        if pontos2 ==10:
            break

#MOSTRANDO PONTUAÇÃO NA TELA
    tela.blit(textoFormatado,(800,40))
    tela.blit(textoFormatado2,(600,40))

    pygame.display.update()