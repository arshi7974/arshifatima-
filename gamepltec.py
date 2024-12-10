# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:01:39 2024

@author: lenovo
"""

import math

# A simple board representation
# X is maximizing, O is minimizing

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if a player has won
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'X'):  # X is the maximizer
        return 10 - depth
    if check_winner(board, 'O'):  # O is the minimizer
        return depth - 10
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):  # Tie condition
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Example of how to use minimax for a Tic-Tac-Toe move
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[row][col] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (row, col)
    return move

# Initialize board with empty spaces
board = [[' ' for _ in range(3)] for _ in range(3)]
print_board(board)
move = best_move(board)
print(f"Best move for 'X': {move}")