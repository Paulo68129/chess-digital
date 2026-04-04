"""
Xadrez digital: jogador vs IA (minimax + alfa-beta).
Regras via python-chess (roque, en passant, empates, etc.).
"""
from __future__ import annotations

import sys
import chess
import pygame
import random

from ai_engine import PROFILES, best_move

CELL = 72
MARGIN_TOP = 100
MARGIN_LEFT = 40
BOARD_PX = 8 * CELL

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
HIGHLIGHT = (186, 202, 68, 120)
LAST_MOVE = (246, 246, 105, 100)
TEXT = (30, 30, 30)
PANEL_BG = (45, 52, 64)

PIECE_CHARS = {
    ("P", True): "\u2659",
    ("N", True): "\u2658",
    ("B", True): "\u2657",
    ("R", True): "\u2656",
    ("Q", True): "\u2655",
    ("K", True): "\u2654",
    ("P", False): "\u265f",
    ("N", False): "\u265e",
    ("B", False): "\u265d",
    ("R", False): "\u265c",
    ("Q", False): "\u265b",
    ("K", False): "\u265a",
}

PROMO_ORDER = [
    (chess.QUEEN, "\u2655"),
    (chess.ROOK, "\u2656"),
    (chess.BISHOP, "\u2657"),
    (chess.KNIGHT, "\u2658"),
]


def square_to_screen(sq: int, human_white: bool) -> tuple[int, int]:
    f, r = chess.square_file(sq), chess.square_rank(sq)
    if human_white:
        col, row = f, 7 - r
    else:
        col, row = 7 - f, r
    x = MARGIN_LEFT + col * CELL
    y = MARGIN_TOP + row * CELL
    return x, y


def screen_to_square(pos: tuple[int, int], human_white: bool) -> int | None:
    x, y = pos
    x -= MARGIN_LEFT
    y -= MARGIN_TOP
    if x < 0 or y < 0 or x >= BOARD_PX or y >= BOARD_PX:
        return None
    col, row = x // CELL, y // CELL
    if human_white:
        f, r = col, 7 - row
    else:
        f, r = 7 - col, row
    return chess.square(f, r)


def piece_char(p: chess.Piece) -> str:
    name = p.symbol().upper()
    return PIECE_CHARS[(name, p.color)]


class Game:
    def __init__(self) -> None:
        self.board = chess.Board()
        self.human_white = True
        self.difficulty = "intermediario"
        self.selected: int | None = None
        self.pending_promos: list[chess.Move] = []
        self.last_move: chess.Move | None = None
        self.status_msg = ""
        self.rng = random.Random()
        self._draw_by_agreement = False
        self._claimed_draw = False

    def human_turn(self) -> bool:
        return (self.board.turn == chess.WHITE) == self.human_white

    def try_move(self, from_sq: int, to_sq: int) -> bool:
        piece = self.board.piece_at(from_sq)
        if piece is None:
            return False
        promos = []
        for m in self.board.legal_moves:
            if m.from_square == from_sq and m.to_square == to_sq:
                if m.promotion:
                    promos.append(m)
                else:
                    self._apply(m)
                    return True
        if promos:
            self.pending_promos = promos
            return True
        return False

    def apply_promotion(self, move: chess.Move) -> None:
        self.pending_promos = []
        self._apply(move)

    def _apply(self, move: chess.Move) -> None:
        self.board.push(move)
        self.last_move = move
        self.selected = None
        self._refresh_status()

    def _refresh_status(self) -> None:
        if self.board.is_checkmate():
            self.status_msg = "Xeque-mate!"
        elif self.board.is_stalemate():
            self.status_msg = "Afogamento — empate."
        elif self.board.is_insufficient_material():
            self.status_msg = "Material insuficiente — empate."
        elif self.board.can_claim_fifty_moves():
            self.status_msg = "50 lances — pode reclamar empate (F4)."
        elif self.board.can_claim_threefold_repetition():
            self.status_msg = "Tripla repetição — pode reclamar empate (F4)."
        elif self.board.is_check():
            self.status_msg = "Xeque."
        else:
            self.status_msg = ""

    def claim_draw(self) -> None:
        o = self.board.outcome(claim_draw=True)
        if o is not None:
            self._claimed_draw = True
            self.status_msg = "Empate reclamado (50 lances ou tripla repetição)."
        else:
            self.status_msg = "Não é possível reclamar empate agora."

    def offer_draw_ai(self) -> None:
        if not self.human_turn() or self.is_over():
            return
        from ai_engine import evaluate_board

        ev = evaluate_board(self.board)
        accept = abs(ev) < 100 or self.rng.random() < 0.2
        if accept:
            self._draw_by_agreement = True
            self.status_msg = "Empate por acordo."
        else:
            self.status_msg = "A IA recusou o empate."

    def is_over(self) -> bool:
        if self._draw_by_agreement or self._claimed_draw:
            return True
        return self.board.is_game_over()

    def ai_play(self) -> None:
        if self.board.is_game_over() or self.human_turn() or self.pending_promos:
            return
        m = best_move(self.board, self.difficulty, self.rng)
        if m:
            self._apply(m)


def pick_font(size: int) -> pygame.font.Font:
    for name in ("Segoe UI Symbol", "DejaVu Sans", "Arial Unicode MS"):
        try:
            return pygame.font.SysFont(name, size)
        except Exception:
            continue
    return pygame.font.Font(None, size)


def draw_board(
    screen: pygame.Surface,
    game: Game,
    font: pygame.font.Font,
    small: pygame.font.Font,
) -> None:
    b = game.board
    human_white = game.human_white

    for sq in chess.SQUARES:
        f, r = chess.square_file(sq), chess.square_rank(sq)
        is_light = (f + r) % 2 == 1
        color = LIGHT if is_light else DARK
        x, y = square_to_screen(sq, human_white)
        pygame.draw.rect(screen, color, (x, y, CELL, CELL))

    if game.last_move:
        for sq in (game.last_move.from_square, game.last_move.to_square):
            x, y = square_to_screen(sq, human_white)
            s = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
            s.fill(LAST_MOVE)
            screen.blit(s, (x, y))

    if game.selected is not None:
        x, y = square_to_screen(game.selected, human_white)
        s = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
        s.fill(HIGHLIGHT)
        screen.blit(s, (x, y))
        for m in b.legal_moves:
            if m.from_square == game.selected:
                tx, ty = square_to_screen(m.to_square, human_white)
                cx, cy = tx + CELL // 2, ty + CELL // 2
                if b.piece_at(m.to_square) is None and not b.is_en_passant(m):
                    pygame.draw.circle(screen, (40, 40, 40), (cx, cy), 10)
                else:
                    pygame.draw.circle(screen, (200, 60, 60), (cx, cy), CELL // 2 - 4, 4)

    for sq in chess.SQUARES:
        p = b.piece_at(sq)
        if p is None:
            continue
        ch = piece_char(p)
        surf = font.render(ch, True, (20, 20, 20))
        x, y = square_to_screen(sq, human_white)
        screen.blit(surf, (x + CELL // 2 - surf.get_width() // 2, y + CELL // 2 - surf.get_height() // 2))

    if game.pending_promos:
        px = MARGIN_LEFT + BOARD_PX // 2 - 2 * CELL
        py = MARGIN_TOP + BOARD_PX + 16
        for i, (ptype, sym) in enumerate(PROMO_ORDER):
            rect = pygame.Rect(px + i * (CELL + 8), py, CELL, CELL - 8)
            pygame.draw.rect(screen, (230, 230, 230), rect)
            pygame.draw.rect(screen, (80, 80, 80), rect, 2)
            s = font.render(sym, True, (0, 0, 0))
            screen.blit(s, (rect.centerx - s.get_width() // 2, rect.centery - s.get_height() // 2))

    panel = pygame.Rect(0, 0, MARGIN_LEFT + BOARD_PX + 280, MARGIN_TOP)
    pygame.draw.rect(screen, PANEL_BG, panel)
    title = small.render("Xadrez — vs IA", True, (220, 220, 230))
    screen.blit(title, (12, 8))
    diff_name = PROFILES[game.difficulty].name
    info = small.render(f"Dificuldade: {diff_name}  (1/2/3)", True, (200, 200, 210))
    screen.blit(info, (12, 32))
    turn = "Sua vez" if game.human_turn() else "IA a jogar..."
    col = (120, 220, 140) if game.human_turn() else (220, 180, 120)
    screen.blit(small.render(turn, True, col), (12, 56))
    if game.status_msg:
        screen.blit(small.render(game.status_msg, True, (255, 200, 120)), (12, 76))
    help_lines = [
        "Cliques: escolher casa e destino",
        "N novo jogo  F virar tabuleiro",
        "D oferecer empate  F4 reclamar empate",
    ]
    hy = MARGIN_TOP + BOARD_PX + 12
    for i, line in enumerate(help_lines):
        screen.blit(small.render(line, True, (180, 180, 190)), (MARGIN_LEFT, hy + i * 22))


def promotion_rects(game: Game) -> list[tuple[pygame.Rect, chess.Move]]:
    if not game.pending_promos:
        return []
    px = MARGIN_LEFT + BOARD_PX // 2 - 2 * CELL
    py = MARGIN_TOP + BOARD_PX + 16
    out: list[tuple[pygame.Rect, chess.Move]] = []
    for i, (ptype, _) in enumerate(PROMO_ORDER):
        rect = pygame.Rect(px + i * (CELL + 8), py, CELL, CELL - 8)
        move = next((m for m in game.pending_promos if m.promotion == ptype), None)
        if move:
            out.append((rect, move))
    return out


def main() -> None:
    pygame.init()
    w = MARGIN_LEFT + BOARD_PX + 40
    h = MARGIN_TOP + BOARD_PX + 140
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Xadrez digital — Jogador vs IA")
    clock = pygame.time.Clock()
    font = pick_font(52)
    small = pick_font(18)
    game = Game()

    while True:
        if not game.human_turn() and not game.is_over() and not game.pending_promos:
            pygame.display.flip()
            game.ai_play()
            game._refresh_status()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    game = Game()
                elif event.key == pygame.K_f:
                    game.human_white = not game.human_white
                elif event.key == pygame.K_1:
                    game.difficulty = "iniciante"
                elif event.key == pygame.K_2:
                    game.difficulty = "intermediario"
                elif event.key == pygame.K_3:
                    game.difficulty = "avancado"
                elif event.key == pygame.K_d:
                    game.offer_draw_ai()
                elif event.key == pygame.K_F4:
                    game.claim_draw()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game.board.is_game_over() or game._draw_by_agreement or game._claimed_draw:
                    continue
                pr = promotion_rects(game)
                for rect, move in pr:
                    if rect.collidepoint(event.pos):
                        game.apply_promotion(move)
                        break
                else:
                    if game.pending_promos:
                        continue
                    if not game.human_turn():
                        continue
                    sq = screen_to_square(event.pos, game.human_white)
                    if sq is None:
                        continue
                    if game.selected is None:
                        p = game.board.piece_at(sq)
                        if p and p.color == (chess.WHITE if game.human_white else chess.BLACK):
                            game.selected = sq
                    else:
                        if sq == game.selected:
                            game.selected = None
                        else:
                            game.try_move(game.selected, sq)

        screen.fill((60, 63, 65))
        draw_board(screen, game, font, small)
        if game.is_over():
            res = "Empate."
            if game._draw_by_agreement:
                res = "Empate por acordo."
            elif game._claimed_draw:
                res = "Empate (reclamação)."
            elif game.board.is_checkmate():
                winner = "Pretas" if game.board.turn == chess.WHITE else "Brancas"
                res = f"Vitória das {winner}."
            elif game.board.is_stalemate() or game.board.is_insufficient_material():
                res = "Empate."
            elif game.board.result() != "*":
                res = f"Resultado: {game.board.result()}"
            overlay = small.render(res + "  (N — novo jogo)", True, (255, 240, 200))
            screen.blit(overlay, (MARGIN_LEFT, 8))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
