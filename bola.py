def mover_bola(bola_x, bola_y,velocidade_bola_x, velocidade_bola_y, gravidade_bola, 
                chao_y, raio_bola, elasticidade_bola, largura):

# movimento vertical
    bola_y += velocidade_bola_y
    velocidade_bola_y += gravidade_bola

# movimento horizontal
    bola_x += velocidade_bola_x

# colisão da bola com o chão
    if bola_y + raio_bola >= chao_y:
        bola_y = chao_y - (raio_bola - 2)
        velocidade_bola_y = -abs(velocidade_bola_x) * elasticidade_bola

    #colisão com a parede direira
    if bola_x + raio_bola >= largura:
        bola_x = largura - raio_bola
        velocidade_bola_x = -abs(velocidade_bola_x)

    #colisão com a parede esqueda
    if bola_x - raio_bola <= 0:
        bola_x = raio_bola
        velocidade_bola_x = abs(velocidade_bola_x)


    return bola_x, bola_y, velocidade_bola_x, velocidade_bola_y


