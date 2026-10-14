# py -3.12 -m pip show pygame
# py -3.12 --version
# py -3.12 [nome do arquivo].py 

import pygame
from jogadores import mover_jogador, pulo_jogador

pygame.init()

largura = 1200
altura = 700

altura_rede = 140
largura_rede = 8

#centro da quadra 600
#centralização da rede (600 - 4) = 596

altura_jogador = 60
largura_jogador = 40

cor_branca = (255, 255, 255)
cor_vermelha = (255, 0, 0)
cor_ceu = (135, 206, 235)
cor_areia = (203, 189, 147)

chao_y = altura - 150
rede_y = chao_y - altura_rede
jogador_y = chao_y - altura_jogador # jogador_y = (700 - 150) - (550 - altura do jogador)

jogador_x_1 = 200
jogador_x_2 = 400

velocidade_jogador = 5

velocidade_y = 0
gravidade = 1
forca_pulo = -12

no_chao = jogador_y == chao_y - altura_jogador

# limite_esquerdo_rede = 
limite_direito_rede = (largura //2 - largura_rede // 2) - largura_jogador
# limites estabelecidos pela rede e a largura do jogador


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

    # pygame.draw.rect( #jogador
    #     tela, cor_vermelha,
    #     (jogador_x_2, jogador_y, largura_jogador, altura_jogador)
    # )


    pygame.display.flip() #apresenta na janela o que desenhamos.
    relogio.tick(60) #limita o laço a aproximadamente 60 repetições por segundo

#=====================================================================================================

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d]:
        direcao = "direita"
        jogador_x_1 = mover_jogador(jogador_x_1, velocidade_jogador, direcao)
        jogador_x_1 = min(jogador_x_1, limite_direito_rede)
            # jogador não pode ultrapassar a rede (x = 596)
            # jogador tem (x = 40) logo (596 - 40 = limite)

    elif teclas[pygame.K_a]:
        direcao = "esquerda"
        jogador_x_1 = mover_jogador(jogador_x_1, velocidade_jogador, direcao)
        jogador_x_1 = max(jogador_x_1, 0)

#=====================================================================================================

    no_chao = jogador_y == chao_y - altura_jogador

    if (teclas[pygame.K_SPACE] or teclas[pygame.K_w]) and no_chao:
        velocidade_y = forca_pulo

    jogador_y, velocidade_y = pulo_jogador(jogador_y,velocidade_y,gravidade,chao_y,altura_jogador)

#=====================================================================================================

pygame.quit()
