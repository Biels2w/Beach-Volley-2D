def trocar_jogador(jogador_ativo):
    if jogador_ativo == 1:
        return 2

    elif jogador_ativo == 2:
        return 1

#===================================================================================

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

#===================================================================================

def moveimentacao_ia(posicao_x, destino_x, velocidade):
    if posicao_x < destino_x:
        posicao_x += velocidade
        posicao_x = min(posicao_x, destino_x)

    elif posicao_x > destino_x:
        posicao_x -= velocidade
        posicao_x = max(posicao_x, destino_x)

    return posicao_x
#===================================================================================
