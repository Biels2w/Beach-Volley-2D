# py -3.12 -m pip show pygame
# py -3.12 --version
# py -3.12 [nome do arquivo].py 

import pygame
from jogadores import mover_jogador, pulo_jogador, trocar_jogador, moveimentacao_ia

pygame.init()

jogador_ativo = 1

posicao_inicial_1 = 200
posicao_inicial_2 = 400

velocidade_ia = 3
#===================================================

largura = 1200
altura = 700

#===================================================

altura_rede = 140
largura_rede = 8
#centro da quadra 600
#centralização da rede (600 - 4) = 596

#===================================================

cor_amarela = (255, 239, 0)
cor_branca = (255, 255, 255)
cor_vermelha = (255, 0, 0)
cor_azul = (65, 105, 225)
cor_ceu = (135, 206, 235)
cor_areia = (203, 189, 147)

#===================================================

chao_y = altura - 150
rede_y = chao_y - altura_rede
# (jogador_y = chao_y - altura_jogador) == [jogador_y = (700 - 150) - (550 - altura do jogador)]

#===================================================

altura_jogador = 60
largura_jogador = 40

# Jogador 1
jogador_x_1 = 200
jogador_y_1 = chao_y - altura_jogador
velocidade_y_1 = 0

# Jogador 2
jogador_x_2 = 400
jogador_y_2 = chao_y - altura_jogador
velocidade_y_2 = 0


#===================================================

velocidade_jogador = 5
gravidade = 1
forca_pulo = -12

linha_identificadora_x = 40
linha_identificadora_y = 10

#===================================================

# limite_esquerdo_rede = 
limite_direito_rede = (largura //2 - largura_rede // 2) - largura_jogador
# limites estabelecidos pela rede e a largura do jogador

#===================================================


tela = pygame.display.set_mode((largura, altura)) #define o tamanho da janela.
pygame.display.set_caption("Beach Volley 2D — Primeiro protótipo") #define o título da janela.

relogio = pygame.time.Clock() #cria um objeto que ajuda a controlar o ritmo do laço.
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                jogador_ativo = trocar_jogador(jogador_ativo)
                print (jogador_ativo)


        if evento.type == pygame.QUIT:
            rodando = False

#=====================================================================================================
#Capta teclas

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d]:
        direcao = "direita"
        if jogador_ativo == 1:
            jogador_x_1 = mover_jogador(jogador_x_1, velocidade_jogador, direcao)
            jogador_x_1 = min(jogador_x_1, limite_direito_rede)

        elif jogador_ativo == 2:
            jogador_x_2 = mover_jogador(jogador_x_2, velocidade_jogador, direcao)
            jogador_x_2 = min(jogador_x_2, limite_direito_rede)
            # jogador não pode ultrapassar a rede (x = 596)
            # jogador tem (x = 40) logo (596 - 40 = limite)

    elif teclas[pygame.K_a]:
        direcao = "esquerda"

        if jogador_ativo == 1:
            jogador_x_1 = mover_jogador(jogador_x_1, velocidade_jogador, direcao)
            jogador_x_1 = max(jogador_x_1, 0)

        elif jogador_ativo == 2:
            jogador_x_2 = mover_jogador(jogador_x_2, velocidade_jogador, direcao)
            jogador_x_2 = max(jogador_x_2, 0)

    if jogador_ativo == 1:
        jogador_x_2 = moveimentacao_ia(jogador_x_2, posicao_inicial_2, velocidade_ia)

    elif jogador_ativo == 2:
        jogador_x_1 = moveimentacao_ia(jogador_x_1, posicao_inicial_1, velocidade_ia)


#=====================================================================================================

    no_chao_1 = jogador_y_1 == chao_y - altura_jogador
    no_chao_2 = jogador_y_2 == chao_y - altura_jogador

    if (teclas[pygame.K_SPACE] or teclas[pygame.K_w]):
        if jogador_ativo == 1 and no_chao_1:
            velocidade_y_1 = forca_pulo

        elif jogador_ativo == 2 and no_chao_2:
            velocidade_y_2 = forca_pulo

    jogador_y_1, velocidade_y_1 = pulo_jogador(jogador_y_1, velocidade_y_1, gravidade, chao_y, altura_jogador)

    jogador_y_2, velocidade_y_2 = pulo_jogador(jogador_y_2, velocidade_y_2, gravidade, chao_y, altura_jogador)

#=====================================================================================================
#Desenha tela
    tela.fill(cor_ceu)

    pygame.draw.rect( #chão
        tela, cor_areia,
        (0, chao_y, largura, altura - chao_y)
    )

    pygame.draw.rect( #rede
        tela, cor_branca,
        (largura //2 - largura_rede // 2, rede_y, largura_rede, altura_rede)
    )

    pygame.draw.rect( #jogador 1
        tela, cor_azul,
        (jogador_x_1, jogador_y_1, largura_jogador, altura_jogador)
    )

    pygame.draw.rect( #jogador
        tela, cor_azul,
        (jogador_x_2, jogador_y_2, largura_jogador, altura_jogador)
    )


#=====================================================================================================

    pygame.display.flip() #apresenta na janela o que desenhamos.
    relogio.tick(60) #limita o laço a aproximadamente 60 repetições por segundo

#=====================================================================================================

pygame.quit()
