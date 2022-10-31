from cProfile import label
import imp


import math
from random import random
import numpy as np
import pygame
import sys
import random

BLUE = (92, 125, 181)
BLACK = (39, 46, 64)
RED = (247, 56, 2)
YELLOW = (236, 240, 22)

# turn
PLAYER = 0
AI = 1
# 1,2 board
PLAYER_PIECE = 1
AI_PIECE = 2


ROW_COUNTS = 6
COLUMN_COUNTS = 7


def create_board():
    board = np.zeros((ROW_COUNTS, COLUMN_COUNTS))
    return board


def drop_piece(board, row, column, piece):  # piece yello or red 1 or 2
    board[row][column] = piece


def is_valid_location(board, column):
    # 0-5 rows and first row
    return board[ROW_COUNTS-1][column] == 0


def get_next_open_row(board, column):
    for r in range(ROW_COUNTS):
        if board[r][column] == 0:  # empty field
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
   # Check horizontal locations for win
    for c in range(COLUMN_COUNTS-3):
        for r in range(ROW_COUNTS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNTS):
        for r in range(ROW_COUNTS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check / diagansol
    for c in range(COLUMN_COUNTS-3):
        for r in range(ROW_COUNTS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check \ diaganols
    for c in range(COLUMN_COUNTS-3):
        for r in range(3, ROW_COUNTS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
# ----------------------------------------------


def score_position(board, piece):
    # horizontal score
    pass

    # ---------------------------------------------


def drow_board(board):
    for column in range(COLUMN_COUNTS):
        for row in range(ROW_COUNTS):
            pygame.draw.rect(screen, BLUE, (column*SQUARESIZE,
                             row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(
                screen, BLACK, (int(column*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    # ------------------------------------------
    for column in range(COLUMN_COUNTS):
        for row in range(ROW_COUNTS):

            if board[row][column] == PLAYER_PIECE:
                pygame.draw.circle(
                    screen, RED, (int(column*SQUARESIZE+SQUARESIZE/2), height - int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[row][column] == AI_PIECE:
                pygame.draw.circle(
                    screen, YELLOW, (int(column*SQUARESIZE+SQUARESIZE/2), height - int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()


board = create_board()
print_board(board)
# print(board)
game_over = False
turn = 0

# GUI-----------------------------------
pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNTS * SQUARESIZE
height = (ROW_COUNTS+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2-5)


screen = pygame.display.set_mode(size)
drow_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 72)
turn = random.randint(PLAYER, AI)


# --------------------------------------
while not game_over:
    for event in pygame.event.get():
        # close
        if event.type == pygame.QUIT:
            sys.exit()

        # scroll btn
        if event.type == pygame.MOUSEMOTION:
            # background top
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(
                    screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(
                    screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        # on click
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

           # Ask for player 1 input
            if turn == PLAYER:

                column = random.randint(0, COLUMN_COUNTS-1)
                # posx = event.pos[0]
                # column = int(math.floor(posx/SQUARESIZE))
                # column = int(input('player 1 make your selection (0 - 6)'))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, PLAYER_PIECE)

                    if winning_move(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 Wins!!!", 1, RED)
                        screen.blit(label, (40, 10))
                        print("Player 1 Wins!!! Congrats :D")
                        game_over = True
                    # change turm
                    turn += 1
                    turn = turn % 2

                    print_board(board)
                    drow_board(board)

    # Ask for player 2 input
    if turn == AI and not game_over:

        column = random.randint(0, COLUMN_COUNTS-1)

        # without random--------------------
        # posx = event.pos[0]
        # column = int(math.floor(posx/SQUARESIZE))
        # comand mode----------------
        # column = int(input('player 2 make your selection (0 - 6)'))
        if is_valid_location(board, column):
            pygame.time.wait(500)
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, AI_PIECE)

            if winning_move(board, AI_PIECE):
                label = myfont.render("Player 2 Wins!!!", 1, YELLOW)
                screen.blit(label, (40, 10))
                print("Player 2 Wins!!! Congrats :D")
                game_over = True

            print_board(board)
            drow_board(board)
            # turn change
            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(5000)
