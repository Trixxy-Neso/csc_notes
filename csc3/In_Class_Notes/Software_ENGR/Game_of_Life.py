import sys
import copy
import os
from time import sleep

def count_neighbors(board, row, column):
    neighbors = 0
    for i in range(-1, 2):
        for j in range (-1, 2):
            if i == 0 and j == 0:
                continue
            elif board [row+i] [column+j] == "*":
                neighbors += 1
    return neighbors

def compute_next (board):
    board_size = len (board)
    next_board = copy.deepcopy (board)

    for row in range (1, board_size-1):
        for column in range (1, board_size-1):
            neighbors = count_neighbors(board, row, column)
            lonely = neighbors < 2
            crowded = neighbors > 3
            perfect_fit = neighbors == 2 or neighbors == 3
            alive = board [row] [column] == "*"
            available = board [row] [column] != "*"

            if alive and (lonely or crowded):
                next_board [row] [column] = " "
            if available and perfect_fit:
                next_board [row] [column] = "*"
    return next_board


def print_board(board):
    board_size = len (board)
    print (" ", end=" ")
    for col_num in range (1, board_size-1):
        print (col_num, end=" ")
    print (" ")
    for row_num, row in enumerate(board):
        if row_num == 0 or row_num == board_size-1:
            continue
        print (row_num, end=" ")
        for col_num, item in enumerate(row):
            if col_num == 0 or col_num == board_size-1:
                continue
            print (item, end=" ")
        print()

GENERATIONS = 25

board = []

for line in sys.stdin:
    content = []
    for character in line:
        if character == "\n":
            continue
        content.append(character)
    board.append (content)

os.system("clear")
print_board (board)
for gen in range (GENERATIONS):
    sleep (0.5)
    os.system("clear")
    board = compute_next(board)
    print_board (board)