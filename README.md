# Beach Volley 2D

Projeto de um jogo de vôlei de praia em duas dimensões, com dois jogadores em cada equipe, a ser desenvolvido com **Python e Pygame**.

O projeto nasce como uma experiência de aprendizado: começar do zero, conhecer o Pygame e construir o jogo gradualmente, registrando o processo no GitHub. Este README documenta a ideia inicial e servirá como referência para acompanhar sua evolução.

## Estado atual

**Protótipo com dois jogadores, seleção e física básica da bola.** Já é possível abrir a janela de 1200 × 700 pixels, visualizar o céu, a areia e a rede, alternar o controle entre dois personagens no lado esquerdo da quadra e movimentá-los ou fazê-los pular. Uma barra amarela menor que a cabeça fica centralizada acima do jogador selecionado e acompanha seus movimentos. O personagem não selecionado retorna à sua posição horizontal inicial. A bola tem gravidade, quiques e colisões com o chão, as paredes laterais e a rede, ainda sujeitas a ajustes.

**Ainda não implementado:** interação entre jogadores e bola, reinício da bola por tecla, equipe adversária, ataques, bloqueios, pontuação, regras de partida e gráficos em pixel art. O retorno do companheiro à posição inicial é um comportamento automático simples; ainda não há adversários controlados pelo computador.

## Tecnologias previstas

| Tecnologia | Papel no projeto | Situação |
| --- | --- | --- |
| Python | Linguagem escolhida para desenvolver o jogo | 3.12 |
| Pygame | Biblioteca escolhida para construir o jogo 2D | 2.6.1  |
| GitHub | Espaço previsto para documentar e acompanhar o desenvolvimento | Repositório criado |


## Funcionalidades planejadas

O conceito central é uma partida de vôlei de praia com duas equipes de dois jogadores. Para transformar essa ideia em um protótipo, estão propostas as seguintes funcionalidades:

- Representação de uma quadra de praia, rede, bola e quatro jogadores em 2D.
- Movimentação dos jogadores e interação com a bola.
- Aperfeiçoamento da física da bola e das colisões, incluindo o contato com os jogadores.
- Identificação de pontos e exibição do placar.
- Início e reinício de uma partida.
- Adversários controlados pelo computador, ataques e bloqueios.
- Personagens e cenário em pixel art, com uma coroa no lugar do indicador provisório.

A perspectiva escolhida é lateral. O protótipo já usa A/D para movimentação, W ou espaço para pular e Tab para alternar entre os dois jogadores. As regras da partida e os controles das futuras ações de vôlei ainda precisam ser definidos. Adversários controlados pelo computador estão planejados; partidas pela internet não fazem parte do escopo definido até aqui.


## Roadmap sugerido

As etapas estão organizadas para permitir aprendizado e validação gradual. Não há datas ou prazos definidos.

### 1. Definir o primeiro protótipo

- [x] Escolher a perspectiva visual do jogo.
- [x] Definir os controles e quais jogadores serão controlados pelo usuário.
- [ ] Estabelecer regras simplificadas e critérios de pontuação.
- [x] Registrar as versões de Python e Pygame utilizadas.

### 2. Criar a base do jogo

- [x] Criar os primeiros arquivos de código.
- [x] Abrir uma janela e implementar o ciclo principal do jogo.
- [x] Desenhar o chão de areia e a rede com formas simples.
- [x] Exibir dois personagens e permitir sua movimentação e seus pulos.
- [x] Identificar o jogador selecionado com uma barra centralizada.
- [x] Iniciar o pulo por pressionamento, verificando o chão a cada atualização.

### 3. Experimentar a interação com a bola

- [x] Adicionar a bola e seu movimento.
- [x] Implementar colisões com o chão, a rede e os jogadores.
- [ ] Permitir a interação entre um jogador e a bola.
- [ ] Ajustar o comportamento do protótipo a partir de testes manuais.

### 4. Construir a partida 2 contra 2

- [ ] Adicionar os quatro jogadores e separar as equipes.
- [ ] Implementar a forma de controle definida na primeira etapa.
- [ ] Adicionar pontuação e reinício após cada ponto.
- [ ] Implementar o encerramento da partida conforme as regras escolhidas.

### 5. Revisar e documentar

- [ ] Revisar controles, colisões e regras da partida.
- [ ] Melhorar a apresentação visual conforme as necessidades do protótipo.
- [x] Documentar a estrutura real dos arquivos e as dependências utilizadas.
- [ ] Incluir instruções verificadas de instalação e execução.
- [ ] Registrar os testes realizados e as limitações conhecidas.

## Preparação e execução

O desenvolvimento usa Python 3.12 e Pygame 2.6.1. Em Windows, os comandos usados para conferir as versões instaladas são:

```bash
py -3.12 --version
py -3.12 -m pip show pygame
```

Para executar o jogo, dentro da pasta do projeto:

```bash
py -3.12 main.py
```


O programa abre o cenário com dois jogadores e uma bola. Use A/D para mover o jogador selecionado, W ou espaço para iniciar um pulo e Tab para trocar o jogador controlado. O pulo é permitido no chão e exige um novo pressionamento após cada salto. Para encerrar, clique no X da janela. A bola ainda não interage com os jogadores e pode parar no chão ou no topo da rede; ainda não há tecla para reiniciá-la. Não há configurações nem variáveis de ambiente definidas, e os requisitos de compatibilidade com outros sistemas ainda não foram verificados.

## Estrutura do projeto

```text
main.py       — abre a janela, trata eventos, integra a lógica e desenha o protótipo
jogadores.py  — movimentação, pulos, troca de jogador e retorno à posição inicial
bola.py       — movimento da bola e colisões com o cenário
README.md     — descrição da ideia, estado atual, roadmap e diário de desenvolvimento
```

A organização de código e recursos será documentada conforme novos arquivos forem criados.

## Diário de desenvolvimento

O diário acompanha o que foi realizado, as dificuldades encontradas e as decisões tomadas. Cada nova entrada deve distinguir resultados concluídos de próximos passos.

### Registro inicial — planejamento

**Realizado:**

- Escolha da ideia de um jogo de vôlei de praia 2D, com dois jogadores por equipe.
- Escolha de Python e Pygame para o desenvolvimento.
- Instalação do Pygame informada pelo autor.
- Preparação da documentação inicial antes da criação do código.

**Contexto de aprendizado:** Iniciando sem conhecimento prévio de Pygame e pretende desenvolver o projeto com orientação gradual.

**Próximo passo proposto:** definir os controles e as regras mínimas do primeiro protótipo.

### Primeira janela com Pygame

**Realizado:**

- Criação do `main.py` com a primeira janela de 1200 × 700 pixels. Escolhi um tamanho maior que o sugerido (960 × 540) pois me agradou mais.
- Cor de fundo em tom de areia, guardada na variável `cor_areia`, com o valor `(203, 189, 147)`.
- Título da janela: "Beach Volley 2D — Primeiro protótipo".
- Laço principal com tratamento do evento `pygame.QUIT` e limite de aproximadamente 60 repetições por segundo.
- Teste manual: a janela abre e fecha corretamente ao clicar no X, sem erros no terminal.

**Aprendizados:**

- O `while rodando` mantém a janela aberta e atende os eventos até o usuário fechar. Sem ele, o programa executaria o código e encerraria logo em seguida.
- `tela.fill(...)` pinta a tela em memória, e `pygame.display.flip()` apresenta na janela o que foi preparado.
- `pygame.quit()` fica depois do laço: ele desliga os módulos do Pygame, então só pode ser chamado quando o jogo não precisa mais deles. Dentro do laço, causaria erro na volta seguinte.

- A origem das coordenadas fica no canto superior esquerdo: `x` aumenta para a direita e `y` aumenta para baixo.
- Um retângulo é descrito por posição horizontal, posição vertical, largura e altura.
- Posição e tamanho são informações diferentes: a base de um retângulo fica em `y + altura_do_retangulo`.
- A ordem do desenho importa: pintar o fundo depois dos objetos apaga o que foi desenhado.
- Variáveis separadas permitem alterar a posição de um jogador sem alterar a do outro.
- As formas simples são representações provisórias para aprender e testar as mecânicas antes da pixel art.

- `pygame.key.get_pressed()` permite verificar continuamente quais teclas estão pressionadas.
- O `main.py` pode importar funções de outro arquivo com `from jogadores import ...`.
- Para limitar a movimentação, é necessário considerar a largura do personagem, e não apenas a posição `x`.
- `min()` e `max()` corrigem posições que passariam dos limites mesmo quando o movimento avança vários pixels por atualização.

- Diminuir `jogador_y` faz o personagem subir; aumentar faz ele descer.
- Uma `velocidade_y` negativa inicia a subida, e a gravidade aumenta essa velocidade gradualmente até começar a descida.
- Velocidade vertical igual a zero no ponto mais alto do salto não significa que o personagem esteja no chão.
- A posição do chão é calculada com `chao_y - altura_jogador`, servindo como limite inferior para o personagem.
- A função de pulo devolve dois valores (`jogador_y` e `velocidade_y`), que precisam ser recebidos no `main.py`.
- O bloco que aplica a gravidade deve executar em todas as atualizações, e não apenas enquanto a tecla de pulo está pressionada.
- Na primeira implementação do pulo, manter a tecla pressionada fazia o personagem iniciar outro salto ao aterrissar. Esse comportamento foi alterado. Início do pulo transferido para o evento `KEYDOWN`, mantendo A/D na consulta contínua de teclas.
- Consultar uma tecla mantida pressionada é diferente de tratar seu pressionamento com `KEYDOWN`.
- Cada lado de uma condição com `or` precisa representar a comparação desejada.
- Uma variável booleana guarda o resultado calculado naquele momento; ela precisa ser recalculada para refletir mudanças na posição.
- A ordem das atualizações influencia o desenho: o indicador deve usar as posições depois dos movimentos e pulos.


**Próximo passo proposto:** criar regras, implementar o reinício da bola com R, antes de revisar a posição anterior usada nas colisões com a rede e adicionar contato entre a bola e os jogadores.

