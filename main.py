# py -3.12 -m pip show pygame
# py -3.12 --version
# py -3.12 [nome do arquivo].py 

import pygame
from jogadores import mover_jogador, pulo_jogador, trocar_jogador, movimentacao_ia
from bola import mover_bola, colisao_rede, reiniciar_bola

pygame.init()

jogador_ativo = 1

posicao_inicial_1 = 200
posicao_inicial_2 = 400

velocidade_ia = 3
#===================================================
#tamanho_tela

largura = 1200
altura = 700

#===================================================
#tamanho rede

altura_rede = 140
largura_rede = 8
#centro da quadra 600
#centralização da rede (600 - 4) = 596

#===================================================
#cores

cor_amarela = (255, 239, 0)
cor_branca = (255, 255, 255)
cor_vermelha = (255, 0, 0)
cor_azul = (65, 105, 225)
cor_ceu = (135, 206, 235)
cor_areia = (203, 189, 147)

#===================================================
#Para a rede ficar acima do chão

chao_y = altura - 150
rede_y = chao_y - altura_rede

#===================================================
#Jogadores

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

# (jogador_y = chao_y - altura_jogador) == [jogador_y = (700 - 150) - (550 - altura do jogador)]
# Para o jogador ficar acima do chão


#===================================================
#Movimentação jogador

velocidade_jogador = 5
gravidade = 1
forca_pulo = -12


#===================================================
#identificador(futura coroa)

espaco = 6 #distancia entre a barra de identificação e a cabeça do jogador

largura_identificador = 16
altura_identificador = 6


#===================================================
#limites rede player

# limite_esquerdo_rede = 
limite_direito_rede = (largura //2 - largura_rede // 2) - largura_jogador 
# limites estabelecidos pela rede e a largura do jogador

#===================================================
#limites rede bola

rede_esquerda = largura // 2 - largura_rede // 2
rede_direita = largura // 2 + largura_rede // 2

rede_inferior = rede_y + altura_rede

# [bola_x + raio_bola >= largura] - colisão lateral parede direita
# [bola_x - raio_bola <= 0] - colisão lateral parede esquerda

#===================================================
#bola

bola_parada = False
raio_bola = 25

bola_x_inicial = 300
bola_y_inicial = 200
velocidade_bola_y_inicial = 0
velocidade_bola_x_inicial = 2

bola_x = bola_x_inicial
bola_y = bola_y_inicial

velocidade_bola_y = velocidade_bola_y_inicial
velocidade_bola_x = velocidade_bola_x_inicial
gravidade_bola = 0.5

elasticidade_bola = 0.35 #multiplicador de altura(y) pós colisão
atrito_bola = 0.85 #conservador da velocidade pós bater na areia
#===================================================

tela = pygame.display.set_mode((largura, altura)) #define o tamanho da janela.
pygame.display.set_caption("Beach Volley 2D — Primeiro protótipo") #define o título da janela.

relogio = pygame.time.Clock() #cria um objeto que ajuda a controlar o ritmo do laço.
rodando = True

while rodando:

    no_chao_1 = jogador_y_1 == chao_y - altura_jogador
    no_chao_2 = jogador_y_2 == chao_y - altura_jogador
    #Atualiza se o jogador está no chão

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                jogador_ativo = trocar_jogador(jogador_ativo) #troca o jogador controlado

#===================================================================================

            if evento.key == pygame.K_SPACE or evento.key == pygame.K_w:
                if jogador_ativo == 1 and no_chao_1:
                    velocidade_y_1 = forca_pulo

                elif jogador_ativo == 2 and no_chao_2:
                    velocidade_y_2 = forca_pulo

#===================================================================================

            if evento.key == pygame.K_r:
                bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, bola_parada = reiniciar_bola(bola_x_inicial, bola_y_inicial, 
    velocidade_bola_x_inicial, velocidade_bola_y_inicial, False
    )

        if evento.type == pygame.QUIT:
            rodando = False
#=====================================================================================================
    bola_x_anterior = bola_x
    bola_y_anterior = bola_y

#Fisica bola

    bola_x, bola_y,velocidade_bola_x, velocidade_bola_y, bola_parada = mover_bola(
    bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, 
    gravidade_bola, chao_y, raio_bola, elasticidade_bola, largura, bola_parada,
    atrito_bola
    )

#Colisão com a rede

    bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, bola_parada = colisao_rede(
        bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, raio_bola, rede_esquerda, 
        rede_direita, rede_y, altura_rede, elasticidade_bola, bola_parada, bola_x_anterior, bola_y_anterior
    )

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
        jogador_x_2 = movimentacao_ia(jogador_x_2, posicao_inicial_2, velocidade_ia)

    elif jogador_ativo == 2:
        jogador_x_1 = movimentacao_ia(jogador_x_1, posicao_inicial_1, velocidade_ia)


#=====================================================================================================
#pulo jogador

    jogador_y_1, velocidade_y_1 = pulo_jogador(jogador_y_1, velocidade_y_1, gravidade, chao_y, altura_jogador)
    jogador_y_2, velocidade_y_2 = pulo_jogador(jogador_y_2, velocidade_y_2, gravidade, chao_y, altura_jogador)

#=====================================================================================================
#identificador jogador

    if jogador_ativo == 1:
        identificador_x = (jogador_x_1 + largura_jogador // 2 - largura_identificador // 2)
        identificador_y = jogador_y_1 - altura_identificador - espaco
    else:
        identificador_x = (jogador_x_2 + largura_jogador // 2 - largura_identificador // 2)
        identificador_y = jogador_y_2 - altura_identificador - espaco
#=====================================================================================================



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

    pygame.draw.rect( #jogador 2
        tela, cor_azul,
        (jogador_x_2, jogador_y_2, largura_jogador, altura_jogador)
    )

    pygame.draw.circle( #bola
        tela, cor_branca, 
        (round(bola_x), round(bola_y)),
        raio_bola
        )

    pygame.draw.rect(
        tela, cor_amarela,
        (identificador_x, identificador_y, 
        largura_identificador, altura_identificador)
    )


#=====================================================================================================

    pygame.display.flip() #apresenta na janela o que desenhamos.
    relogio.tick(60) #limita o laço a aproximadamente 60 repetições por segundo

#=====================================================================================================

pygame.quit()
