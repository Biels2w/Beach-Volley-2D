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
                altura_rede, elasticidade_bola, bola_parada):

    # Guarda a posição anterior da bola
    anterior_x = bola_x - velocidade_bola_x
    anterior_y = bola_y - velocidade_bola_y

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

