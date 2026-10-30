# ===IMPORTANDO=
import pygame
from pygame.locals import *
#importando tudo do py game!
from sys import exit
# importando a função de fechar a janela

#começando, inicializando as funções

pygame.init()

#criando a tela, o pygame seta o modo de tela com a largura e altura
# com esse comando "tela = pygame.display.set_mode((640,480))"
# mas como o professor é loko e adora complicar nossa vida vamos criar variaveis para isso

largura = 640
altura = 480
tela = pygame.display.set_mode((largura,altura))

# criando o loop para detectar algum evento
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()    
            exit()
    
    # desenhando um retângulo e um circulo
    #o primeiro parametro e segundo sao x e y o terceiro é a largura em px, e o quarto a altura

    pygame.draw.rect(tela, (255,0,0), (200,300,40,50))
    # no caso do circulo o ultimo parametro é o raio.
    pygame.draw.circle(tela, (0,20, 200), (200,230), 30)
    # criando um linha, cor, posição inicial, posiçao final, 
    pygame.draw.line(tela, (20,20,20), (100, 390), (0, 90), 5)
    pygame.display.update()
    #A cada interção ele atualiaza para nao haver nenhum tipo de erro, como por exemplo se o jogo travar.