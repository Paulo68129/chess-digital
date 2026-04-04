# Xadrez digital — Jogador vs IA

Jogo de xadrez para desktop com interface gráfica (Pygame), modo **humano contra máquina** e regras oficiais garantidas pela biblioteca **python-chess**.

---

## Autoria

**Paulo Roberto** — concepção, implementação e documentação deste projeto.

As bibliotecas de terceiros utilizadas (`python-chess`, `pygame`) mantêm as respetivas licenças e créditos dos autores originais.

---

## Funcionalidades

- Tabuleiro 8×8 com orientação correta (casa clara em **h1**).
- Todas as regras habituais: movimentos das peças, **roque**, **en passant**, **promoção** (Dama, Torre, Bispo, Cavalo), **xeque** e **xeque-mate**.
- Situações de **empate**: afogamento, material insuficiente, oferta de empate à IA, reclamação de empate (50 lances / tripla repetição quando aplicável).
- **IA** com algoritmo **minimax** e **poda alfa-beta**, com três níveis: iniciante, intermediário e avançado.

---

## Requisitos

- Python 3.10 ou superior (recomendado).
- Sistema com suporte a janelas gráficas (para o Pygame).

---

## Instalação

```bash
cd chess-digital
python -m pip install -r requirements.txt
```

---

## Como executar

```bash
python main.py
```

---

## Controles

| Tecla | Ação |
|--------|------|
| **Cliques** | Selecionar peça e casa de destino |
| **1 / 2 / 3** | Dificuldade: iniciante / intermediário / avançado |
| **N** | Novo jogo |
| **F** | Inverter o tabuleiro (jogar com as brancas ou pretas na base) |
| **D** | Oferecer empate à IA |
| **F4** | Reclamar empate (quando a posição o permitir) |

Na **promoção** de peão, escolha a peça nos botões abaixo do tabuleiro.

---

## Estrutura do projeto

| Ficheiro | Descrição |
|----------|-----------|
| `main.py` | Interface Pygame, ciclo de jogo e interação com o utilizador |
| `ai_engine.py` | Motor de IA (avaliação, minimax, níveis de dificuldade) |
| `requirements.txt` | Dependências Python |

---

## Tecnologias

- **[python-chess](
)** — lógica do jogo e legalidade dos lances.
- **[pygame](https://www.pygame.org/)** — janela, desenho do tabuleiro e entrada do rato/teclado.

---

## Licença

Código original por **Paulo Roberto**. Define à vontade uma licença explícita (por exemplo MIT ou GPL) num ficheiro `LICENSE` se quiseres distribuir o projeto com termos claros.
