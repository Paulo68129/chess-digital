# ♟️ chess-digital

**Xadrez digital — Jogador vs IA (Desktop / Python)**

Jogo de xadrez para desktop com **interface gráfica em Pygame**, **IA própria baseada em Minimax com poda alfa–beta** e **regras oficiais garantidas pela biblioteca `python-chess`**.

Projetado para partidas **Humano vs Máquina**, o projeto combina **correção das regras**, **algoritmos clássicos de Inteligência Artificial** e uma **experiência de jogo fluida em ambiente desktop offline**.

***

## 🖥️ Demonstração

>  *(<img width="244" height="239" alt="image" src="https://github.com/user-attachments/assets/708ba004-c276-499b-aef0-bb199687ff54" />
)*

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

Código original desenvolvido por **Paulo Roberto S**.

Copyright (C) 2026 Paulo Roberto

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
``
` ao repositório  
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
