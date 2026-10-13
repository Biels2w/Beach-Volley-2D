# py -3.12 -m pip show pygame
# py -3.12 --version
# py -3.12 [nome do arquivo].py 

import pygame

cor_areia = (203, 189, 147)

pygame.init()

largura = 1200
altura = 700

tela = pygame.display.set_mode((largura, altura)) #define o tamanho da janela.
pygame.display.set_caption("Beach Volley 2D — Primeiro protótipo") #define o título da janela.

relogio = pygame.time.Clock() #cria um objeto que ajuda a controlar o ritmo do laço.
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(cor_areia)
    pygame.display.flip() #apresenta na janela o que desenhamos.
    relogio.tick(60) #limita o laço a aproximadamente 60 repetições por segundo

pygame.quit()
