import mesa
from random_move import RandomWalker
import random


class Board(mesa.Agent):
    def __init__(self, unique_id, model):
        self.width = 7
        self.height = 6
        self.ROW_COUNTS = 6
        self.COLUMN_COUNTS = 7
        # initialize the parent class with required parameters
        super().__init__(unique_id, model)
        self.grid = mesa.space.SingleGrid(
            self.COLUMN_COUNTS, self.ROW_COUNTS, torus=True)

    def evaluat_board(Rules):
        pass

    def get_next_open_row(self, column):
        for r in range(0, self.ROW_COUNTS-1):
            if self.grid.is_cell_empty((r, column)):
                print("get next", r, column)
                return r

    def drop_piece(self, id, row, column, piece):
        return Player(id, (row, column), self, True, self.grid, type=piece)

# subclass of RandomWalker, which is subclass to Mesa Agent


class Player(RandomWalker):
    def __init__(self, unique_id, pos, model, moore, board, type):
        # init parent class with required parameters
        super().__init__(unique_id, pos, model, moore=moore)
        # the amount each person has in savings
        self.type = type
        self.board = board
  # step is called for each agent in model.Board.schedule.step()

    def step(self):
        print("step agent")
        # move to a cell in my Moore neighborhood
        # self.random_move()

        # self.board.evaluat_board()
