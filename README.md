# ♟️ chess-digital

**Xadrez digital — Jogador vs IA (Desktop / Python)**

Jogo de xadrez para desktop com **interface gráfica em Pygame**, **IA própria baseada em Minimax com poda alfa–beta** e **regras oficiais garantidas pela biblioteca `python-chess`**.

Projetado para partidas **Humano vs Máquina**, o projeto combina **correção das regras**, **algoritmos clássicos de Inteligência Artificial** e uma **experiência de jogo fluida em ambiente desktop offline**.

***

## 🖥️ Demonstração

> 📌 *(Adicione aqui 1 ou 2 screenshots e, opcionalmente, um GIF curto do jogo em andamento)*

```text
[Screenshot do tabuleiro em jogo]
[GIF curto mostrando uma jogada do jogador e a resposta da IA]
```

***

## 🎯 Objetivos do Projeto

*   Implementar um jogo de xadrez **com regras oficiais completas**
*   Desenvolver uma **IA própria**, sem uso de motores externos
*   Criar uma aplicação **desktop funcional e estável**
*   Servir como **projeto educacional, de portfólio e base evolutiva**

***

## ✨ Funcionalidades

### ♜ Regras Oficiais (via `python-chess`)

*   Movimentos legais de todas as peças
*   Roque (curto e longo)
*   En passant
*   Promoção de peão (Dama, Torre, Bispo ou Cavalo)
*   Xeque e xeque-mate

### ♟️ Situações de Empate

*   Afogamento (stalemate)
*   Material insuficiente
*   Regra dos 50 lances
*   Tripla repetição
*   Oferta de empate à IA
*   Reclamação manual de empate quando aplicável

### 🧠 Inteligência Artificial

*   Algoritmo **Minimax**
*   **Poda alfa–beta** para otimização
*   Avaliação heurística de posições
*   Três níveis de dificuldade:
    *   🟢 Iniciante
    *   🟡 Intermediário
    *   🔴 Avançado

### 🎮 Interface Gráfica (Pygame)

*   Tabuleiro 8×8 com orientação correta (casa clara em **h1**)
*   Interação por mouse (seleção de peça e destino)
*   Botões gráficos para promoção de peão
*   Inversão do tabuleiro (jogar com brancas ou pretas na base)
*   Controles por teclado para ações rápidas

***

## ⌨️ Controles

| Tecla / Ação    | Descrição                                         |
| --------------- | ------------------------------------------------- |
| Clique do mouse | Selecionar peça e casa de destino                 |
| `1` / `2` / `3` | Dificuldade: Iniciante / Intermediário / Avançado |
| `N`             | Novo jogo                                         |
| `F`             | Inverter orientação do tabuleiro                  |
| `D`             | Oferecer empate à IA                              |
| `F4`            | Reclamar empate (quando permitido)                |

> Na promoção de peão, a escolha da peça é feita pelos botões exibidos abaixo do tabuleiro.

***

## 🧱 Estrutura do Projeto

    chess-digital/
    │
    ├── main.py           # Interface Pygame, loop principal e interação
    ├── ai_engine.py      # Motor de IA (avaliação, minimax, níveis)
    ├── requirements.txt  # Dependências do projeto
    └── README.md

***

## 🛠️ Tecnologias Utilizadas

*   **Python 3.10+**
*   **pygame** — Interface gráfica e entrada do utilizador
*   **python-chess** — Lógica do jogo, validação de lances e regras oficiais

***

## ⚙️ Requisitos

*   Python **3.10 ou superior** (recomendado)
*   Sistema operacional com suporte a janelas gráficas (Pygame)

***

## 📦 Instalação

```bash
cd chess-digital
python -m pip install -r requirements.txt
```

***

## ▶️ Como Executar

```bash
python main.py
```

***

## 👤 Autoria

**Paulo Roberto**  
Concepção, implementação e documentação deste projeto.

As bibliotecas de terceiros utilizadas (**python-chess**, **pygame**) mantêm as respetivas licenças e créditos dos seus autores originais.

***

## 📜 Licença

Código original desenvolvido por **Paulo Roberto**.

> 📌 Recomenda-se adicionar um ficheiro `LICENSE` ao repositório  
> Sugestões:

*   **MIT License** — uso livre, ideal para portfólio e reutilização
*   **GPL v3** — garante que derivados permaneçam open source

***

## 🚀 Possíveis Evoluções

*   Sistema de tempo (relógio de xadrez)
*   Extração/exportação de partidas (PGN)
*   Ajustes avançados na heurística da IA
*   Multiplayer local ou online
*   Interface gráfica mais avançada (menus, temas)

***

### ♟️ Considerações Finais

Este projeto demonstra:

*   Domínio de **algoritmos clássicos de IA**
*   Correção rigorosa das **regras do xadrez**
*   Boa arquitetura e separação de responsabilidades
*   Capacidade de entregar uma **aplicação desktop completa**

Ideal como **projeto de portfólio**, **base acadêmica** ou **produto educacional**.

***
