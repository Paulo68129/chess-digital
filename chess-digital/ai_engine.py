"""
Motor de xadrez: minimax com poda alfa-beta e níveis de dificuldade.
Avaliação por material + tabelas de casas (piece-square tables) simplificadas.
"""
from __future__ import annotations

import chess
import random
from dataclasses import dataclass
from typing import Optional

# Valores de material (centipawns)
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0,
}

# Tabelas para peão (perspectiva branca; espelhamos para pretas)
PAWN_TABLE = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 25, 25, 10, 5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 10, 10, -20, -20, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0,
]

KNIGHT_TABLE = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

BISHOP_TABLE = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]


def _pst_for_piece(piece_type: int, square: int, color: chess.Color) -> int:
    r = chess.square_rank(square)
    f = chess.square_file(square)
    if color == chess.BLACK:
        r = 7 - r
    tidx = r * 8 + f
    if piece_type == chess.PAWN:
        return PAWN_TABLE[tidx]
    if piece_type == chess.KNIGHT:
        return KNIGHT_TABLE[tidx]
    if piece_type == chess.BISHOP:
        return BISHOP_TABLE[tidx]
    return 0


def _absolute_material(board: chess.Board) -> int:
    """Material + PST: positivo = vantagem das brancas."""
    score = 0
    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p is None:
            continue
        v = PIECE_VALUES[p.piece_type] + _pst_for_piece(p.piece_type, sq, p.color)
        if p.color == chess.WHITE:
            score += v
        else:
            score -= v
    return score


def evaluate_board(board: chess.Board) -> int:
    """
    Avaliação na perspectiva de quem está a jogar (positivo = bom para o lado a mover).
    """
    if board.is_checkmate():
        return -30000
    if board.is_stalemate() or board.is_insufficient_material():
        return 0
    w = _absolute_material(board)
    return w if board.turn == chess.WHITE else -w


@dataclass
class DifficultyProfile:
    name: str
    max_depth: int
    noise_cp: int  # aleatoriedade em centipawns (0 = determinístico)
    mistake_rate: float  # probabilidade de jogada subótima no nível iniciante


PROFILES = {
    "iniciante": DifficultyProfile("Iniciante", max_depth=2, noise_cp=40, mistake_rate=0.22),
    "intermediario": DifficultyProfile("Intermediário", max_depth=3, noise_cp=12, mistake_rate=0.06),
    "avancado": DifficultyProfile("Avançado", max_depth=4, noise_cp=0, mistake_rate=0.0),
}


def _negamax(board: chess.Board, depth: int, alpha: int, beta: int) -> int:
    if depth == 0:
        return evaluate_board(board)

    moves = list(board.legal_moves)
    if not moves:
        return evaluate_board(board)

    best = -999999
    for move in moves:
        board.push(move)
        val = -_negamax(board, depth - 1, -beta, -alpha)
        board.pop()
        best = max(best, val)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return best


def _order_moves(board: chess.Board, moves: list) -> list:
    def score_move(m: chess.Move) -> int:
        s = 0
        if board.is_capture(m):
            victim = board.piece_at(m.to_square)
            attacker = board.piece_at(m.from_square)
            if victim:
                s += 10 * PIECE_VALUES.get(victim.piece_type, 0) - PIECE_VALUES.get(
                    attacker.piece_type if attacker else chess.PAWN, 0
                )
        if board.gives_check(m):
            s += 50
        return -s

    return sorted(moves, key=score_move)


def best_move(
    board: chess.Board,
    profile_key: str = "intermediario",
    rng: Optional[random.Random] = None,
) -> Optional[chess.Move]:
    """
    Escolhe a melhor jogada legal para o lado que está a jogar em `board.turn`.
    """
    rng = rng or random.Random()
    profile = PROFILES.get(profile_key, PROFILES["intermediario"])
    legal = list(board.legal_moves)
    if not legal:
        return None

    if rng.random() < profile.mistake_rate and len(legal) > 1:
        return rng.choice(legal)

    depth = profile.max_depth
    best_val = -10**9
    candidates: list[tuple[int, chess.Move]] = []

    ordered = _order_moves(board, legal)
    for move in ordered:
        board.push(move)
        val = -_negamax(board, depth - 1, -10**9, 10**9)
        board.pop()
        if val > best_val:
            best_val = val
            candidates = [(val, move)]
        elif val == best_val:
            candidates.append((val, move))

    if not candidates:
        return legal[0]

    if profile.noise_cp > 0:
        filtered = [
            (v, m) for v, m in candidates if v >= best_val - profile.noise_cp
        ]
        choice = rng.choice(filtered if filtered else candidates)
        return choice[1]

    return candidates[0][1]
