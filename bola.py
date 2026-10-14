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


