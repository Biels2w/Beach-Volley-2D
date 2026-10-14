def mover_jogador(posicao_x_1, velocidade_jogador, direcao):
    if direcao == "direita":
        posicao_x_1 += velocidade_jogador
    elif direcao == "esquerda":
        posicao_x_1 -= velocidade_jogador

    return posicao_x_1

#===================================================================================


def pulo_jogador(jogador_y, velocidade_y, gravidade, chao_y, altura_jogador):

    jogador_y += velocidade_y

    velocidade_y += gravidade

# verifica se está no chão
    if jogador_y >= chao_y - altura_jogador:
        jogador_y = chao_y - altura_jogador
        velocidade_y = 0

    return jogador_y, velocidade_y

