def mover_bola(bola_x, bola_y,velocidade_bola_x, velocidade_bola_y, gravidade_bola, 
                chao_y, raio_bola, elasticidade_bola, largura, bola_parada, atrito_bola):

# movimento vertical
    if not bola_parada:
        bola_y += velocidade_bola_y
        velocidade_bola_y += gravidade_bola

# colisão da bola com o chão
    if not bola_parada and bola_y + raio_bola >= chao_y and velocidade_bola_y > 0:
        bola_y = chao_y - raio_bola

        velocidade_bola_x *= atrito_bola
        velocidade_bola_y = -velocidade_bola_y * elasticidade_bola

        if abs(velocidade_bola_y) < 1:
            velocidade_bola_y = 0
            velocidade_bola_x = 0
            bola_parada = True

    # movimento horizontal
    bola_x += velocidade_bola_x

    #colisão com a parede direira
    if bola_x + raio_bola >= largura:
        bola_x = largura - raio_bola
        velocidade_bola_x = -abs(velocidade_bola_x)

    #colisão com a parede esqueda
    if bola_x - raio_bola <= 0:
        bola_x = raio_bola
        velocidade_bola_x = abs(velocidade_bola_x)


    return bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, bola_parada


#============================================================================================

def colisao_rede(bola_x, bola_y, velocidade_bola_x, velocidade_bola_y,
                raio_bola, rede_esquerda, rede_direita, rede_y,
                altura_rede, elasticidade_bola, bola_parada, 
                anterior_x, anterior_y):

    rede_inferior = rede_y + altura_rede

    # Verifica se a bola chegou na rede:
    colisao =(
        bola_x + raio_bola >= rede_esquerda and
        bola_x - raio_bola <= rede_direita and
        bola_y + raio_bola >= rede_y and
        bola_y - raio_bola <= rede_inferior
    )

    if colisao:
        if(velocidade_bola_y > 0 and anterior_y + raio_bola <= rede_y):

            bola_y = rede_y - raio_bola
            velocidade_bola_y = -abs(velocidade_bola_y) * elasticidade_bola
            velocidade_bola_x *= 0.85

            if abs(velocidade_bola_y) < 3:
                velocidade_bola_y = 0
                velocidade_bola_x = 0
                bola_parada = True

        # Colisão com a lateral esquerda
        elif velocidade_bola_x > 0 and anterior_x + raio_bola <= rede_esquerda:

            bola_x = rede_esquerda - raio_bola
            velocidade_bola_x = -abs(velocidade_bola_x)

        # Colisão com a lateral direita
        elif velocidade_bola_x < 0 and anterior_x - raio_bola >= rede_direita:

            bola_x = rede_direita + raio_bola
            velocidade_bola_x = abs(velocidade_bola_x)

    return bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, bola_parada

#============================================================================================
#Reiniciar bola

def reiniciar_bola(bola_x_inicial, bola_y_inicial, velocidade_bola_x_inicial, velocidade_bola_y_inicial, bola_parada):

    return bola_x_inicial, bola_y_inicial, velocidade_bola_x_inicial, velocidade_bola_y_inicial, bola_parada

#============================================================================================
#colisão bola jogador

def colisao_jogador(
    bola_x, bola_y, velocidade_bola_y, raio_bola,
    bola_y_anterior, jogador_x, jogador_y,
    largura_jogador, bola_parada, jogador_y_anterior
):
    # Borda esquerda jogador
    jogador_esquerda = jogador_x
    jogador_direita = jogador_x + largura_jogador

    # X = centro da bola.
    # Subtrair e somar o raio encontra bordas.
    bola_esquerda = bola_x - raio_bola
    bola_direita = bola_x + raio_bola

    # A bola precisa ocupar parte da faixa horizontal do jogador.
    sobreposicao_x = (
        bola_direita >= jogador_esquerda
        and bola_esquerda <= jogador_direita
    )

    # Parte da bola (baixo) que colide com o jogador.
    bola_base_anterior = bola_y_anterior + raio_bola
    bola_base_atual = bola_y + raio_bola

    # Antes, a bola estava acima da cabeça.
    # Agora, chegou a cabeça ou passou um pouco dela.
    cruzou_cabeca = (
        bola_base_anterior <= jogador_y_anterior
        and bola_base_atual >= jogador_y
    )

    # Versão que só aceita a bola descendo.
    # Velocidade vertical positiva significa movimento para baixo.
    descendo = velocidade_bola_y > 0

    if sobreposicao_x and cruzou_cabeca and descendo:
        # Corrige a posição para a bola não ficar dentro do jogador.
        bola_y = jogador_y - raio_bola

        # Valor negativo faz a bola subir.
        velocidade_bola_y = -10

        # Fisica ainda ativa
        bola_parada = False

    # Devolvemos o estado, mesmo quando não houve contato.
    return bola_y, velocidade_bola_y, bola_parada