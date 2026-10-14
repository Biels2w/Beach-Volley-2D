# py -3.12 -m pip show pygame
# py -3.12 --version
# py -3.12 [nome do arquivo].py 

import pygame

pygame.init()

largura = 1200
altura = 700

altura_rede = 140
largura_rede = 8

altura_jogador = 60
largura_jogador = 40

cor_branca = (255, 255, 255)
cor_vermelha = (255, 0, 0)
cor_ceu = (135, 206, 235)
cor_areia = (203, 189, 147)

chao_y = altura - 150
rede_y = chao_y - altura_rede
jogador_y = chao_y - altura_jogador

jogador_x_1 = 200
jogador_x_2 = 400


tela = pygame.display.set_mode((largura, altura)) #define o tamanho da janela.
pygame.display.set_caption("Beach Volley 2D — Primeiro protótipo") #define o título da janela.

relogio = pygame.time.Clock() #cria um objeto que ajuda a controlar o ritmo do laço.
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


#=====================================================================================================
    tela.fill(cor_ceu)

    pygame.draw.rect( #chão
        tela, cor_areia,
        (0, chao_y, largura, altura - chao_y)
    )

    pygame.draw.rect( #rede
        tela, cor_branca,
        (largura //2 - largura_rede // 2, rede_y, largura_rede, altura_rede)
    )

    pygame.draw.rect( #jogador
        tela, cor_vermelha,
        (jogador_x_1, jogador_y, largura_jogador, altura_jogador)
    )

    pygame.draw.rect( #jogador
        tela, cor_vermelha,
        (jogador_x_2, jogador_y, largura_jogador, altura_jogador)
    )


    pygame.display.flip() #apresenta na janela o que desenhamos.
    relogio.tick(60) #limita o laço a aproximadamente 60 repetições por segundo

#=====================================================================================================

pygame.quit()
