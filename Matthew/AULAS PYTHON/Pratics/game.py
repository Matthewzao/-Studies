import pygame
from sys import exit

# INICIALIZANDO O PYGAME
pygame.init()

screen = pygame.display.set_mode((1600, 900))

pygame.display.set_caption("Matthew's Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen, (255,0,0), (400,500,40,50))
    pygame.draw.circle(screen,(0,0,255),(300,260),40)
    pygame.draw.line(screen,(255,255,0),(390,0),(390,600),)

    pygame.display.update()
