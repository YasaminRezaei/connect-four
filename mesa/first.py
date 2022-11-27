from cProfile import label
import imp
import math
from random import random
import numpy as np
import pygame
import sys
import random

# farbinformation GUI
BLUE = (92, 125, 181)
BLACK = (39, 46, 64)
RED = (247, 56, 2)
YELLOW = (236, 240, 22)

# turn wird jedes mal gewechselt
PLAYER1 = 0
PLAYER2 = 1

# board besteht aus 0, 1,2
EMPTY = 0
PLAYER_PIECE1 = 1
PLAYER_PIECE2 = 2

# 4 connect
WINDOW_LENGTH = 4

# anzahl von rows und columns
ROW_COUNTS = 6
COLUMN_COUNTS = 7

# create_board
# am Anfang haben wir ein leeres board


def create_board():
    board = np.zeros((ROW_COUNTS, COLUMN_COUNTS))
    return board
# -------------------------------------------------
# drop_piece
# piece yello or red, 1 or 2, also PLAYER_PIECE1 und PLAYER_PIECE2
# hier wird in board[row][column] , 1 oder 2 gesetzt.


def drop_piece(board, row, column, piece):
    board[row][column] = piece

# ------------------------------------------------
# is_valid_location
# hier wird geprüft, ob Feld leer ist?


def is_valid_location(board, column):
    # 0-5 rows and first row
    return board[ROW_COUNTS-1][column] == 0

# ------------------------------------------------
# get_next_open_row
# hier wird nechste offene row,dass empty ist, gezeigt


def get_next_open_row(board, column):
    for row in range(ROW_COUNTS):
        if board[row][column] == 0:  # empty field
            return row

# ------------------------------------------------
# print_board
# hier wird bord umgekehr gezeigt.


def print_board(board):
    print(np.flip(board, 0))

# ------------------------------------------------
# winning_move
# hier wird überprüft, ob wir 4 in row oder column oder diagonal haben oder nicht?


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
 # evaluated window für player 1
 # hier evaluieren wir unser board.bei rot oder gelb, wir geben score.
 # connect 4 ->100
 # connect 3 ->10
 # connect 2 -> 5


def evaluate_window(window, piece):
    score = 0
    # gegner definieren
    opponet_piece = PLAYER_PIECE1
    if piece == PLAYER_PIECE1:
        opponet_piece = PLAYER_PIECE2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5
    # verteidiger ? block if i get 3 in row
    if window.count(opponet_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80
    return score

# ----------------------------------------------
# score


def score_position(board, piece):
    score = 0
    # center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNTS//2])]
    center_count = center_array.count(piece)
    score += center_count * 6  # in mittle ist immer besser

    # horizontal score
    for row in range(ROW_COUNTS):
        row_array = [int(i) for i in list(board[row, :])]
        for column in range(COLUMN_COUNTS-3):
            window = row_array[column:column+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # vertical score
    for column in range(COLUMN_COUNTS):
        column_array = [int(i) for i in list(board[:, column])]
        for row in range(ROW_COUNTS-3):
            window = column_array[row: row + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # diagonal /
    for row in range(ROW_COUNTS-3):
        for column in range(COLUMN_COUNTS-3):
            window = [board[row+i][column+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # diagonal \
    for row in range(ROW_COUNTS-3):
        for column in range(COLUMN_COUNTS-3):
            window = [board[row+3 - i][column+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


# ---------------------------------------------
# pic best move
# hier wird board überprüft und wird best move nach score ausgewählt
def pick_best_move(board, piece):

    valid_locations = get_valid_locations(board)
    best_score = 100000  # not negativ
    best_column = random.choice(valid_locations)
    for column in valid_locations:
        row = get_next_open_row(board, column)
        temp_board = board.copy()
        drop_piece(temp_board, row, column, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_column = column
    return best_column

# ----------------------------------------------
# get valid locations
# hier bekommen wir ein array von mögliche locations


def get_valid_locations(board):
    valid_locations = []
    for column in range(COLUMN_COUNTS):
        if is_valid_location(board, column):
            valid_locations.append(column)
    return valid_locations

# ----------------------------------------------
# GUI


def drow_board(board):
    for column in range(COLUMN_COUNTS):
        for row in range(ROW_COUNTS):
            pygame.draw.rect(screen, BLUE, (column*SQUARESIZE,
                             row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(
                screen, BLACK, (int(column*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for column in range(COLUMN_COUNTS):
        for row in range(ROW_COUNTS):

            if board[row][column] == PLAYER_PIECE1:
                pygame.draw.circle(
                    screen, RED, (int(column*SQUARESIZE+SQUARESIZE/2), height - int(row*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[row][column] == PLAYER_PIECE2:
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
turn = random.randint(PLAYER1, PLAYER2)


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
            if turn == PLAYER1:
                pygame.draw.circle(
                    screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(
                    screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        # controllieren
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

           # Ask for player 1 input
            if turn == PLAYER1:
                column = pick_best_move(board, PLAYER_PIECE1)
                if is_valid_location(board, column):
                    pygame.time.wait(2000)
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, PLAYER_PIECE1)

                    if winning_move(board, PLAYER_PIECE1):
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
    if turn == PLAYER2 and not game_over:

        #column = random.randint(0, COLUMN_COUNTS-1)
        column = pick_best_move(board, PLAYER_PIECE2)

        if is_valid_location(board, column):
            pygame.time.wait(2000)
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, PLAYER_PIECE2)

            if winning_move(board, PLAYER_PIECE2):
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
        pygame.time.wait(10000)
