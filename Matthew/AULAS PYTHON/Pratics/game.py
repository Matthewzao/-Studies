import pygame
from sys import exit

# INICIALIZANDO O PYGAME
pygame.init()

altura = 1000
largura = 900
tela = pygame.display.set_mode((altura,largura))                # DETERMINA O TAMANHO DA TELA
x = largura /4 # centralizando objeto
y = 0
a = 0
b = 0

pygame.display.set_caption("Matthew's Game")
relogio = pygame.time.Clock()                                   #ADICIONANDO UM FPS

while True:
    relogio.tick(60)                                            #CONTROLANDO O FPS   
    tela.fill((0,0,0))                                          #AQUI DETERMINA QUE A PARTE PRETA PREENCHA O RESTO DA TELA, PARA DAR O EFEITO DE ANIMAÇÃO
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                           #PARA O PROGRAMA FECHAR QUANDO CLICADO NO X
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    pygame.draw.rect(tela, (255,0,0), (b,a,40,50))              # ADICIONANDO OUTRO OBJETO

                                                                # DETERMINA O LOOP DA ANIMAÇÃO
    if y >= altura:
        y = 0        
    y = y+20                                                    # CONTROLA A VELOCIDADE DO OBJETO

    if a >= altura:
        a = 0
    a=a+5

    
    pygame.display.update()    






    # pygame.draw.circle(screen,(0,0,255),(300,260),40) PARA DESENHAR UM CIRCULO
    # pygame.draw.line(screen,(255,255,0),(390,0),(390,600),) PARA DESENHAR UMA LINHA