import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 480
largura = 640

x = largura/2
y = 0 
tela = pygame.display.set_mode((largura,altura))
while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()    
            exit()
    pygame.draw.rect(tela, (200,20,30), (x,y,100,100))
    if y>= altura:
        y = 0
    # se o y for igual a altura ou maior ele retorna para o eixo 0
    y = y+0.2

    pygame.display.update()

# meio = larguraTela/2 - larguraOBJ/2