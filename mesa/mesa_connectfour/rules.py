import mesa
from agents import Player


class Rules():
    ROW_COUNTS = 6
    COLUMN_COUNTS = 7

    def __init__(self, model):
        self.game_over = False
        super().__init__(model)
        self.grid = mesa.space.SingleGrid(
            self.COLUMN_COUNTS, self.ROW_COUNTS, torus=True)

    def is_valid_location(self, column):
        pos = (5, column)
        print("pos", pos)
        print('--->', self.grid.is_cell_empty(pos))
        return self.grid.is_cell_empty(pos)

    def winning_move(self, piece):
        for c in range(self.COLUMN_COUNTS-3):
            for r in range(self.ROW_COUNTS):
                if Player(r, c).type == piece and Player(r, c+1).type == piece and Player(r, c+2).type == piece and Player(r, c+3).type == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.COLUMN_COUNTS):
            for r in range(self.ROW_COUNTS-3):
                if Player(r, c).type == piece and Player(r+1, c).type == piece and Player(r+2, c).type == piece and Player(r+3, c).type == piece:
                    return True

        # Check / diagansol
        for c in range(self.COLUMN_COUNTS-3):
            for r in range(self.ROW_COUNTS-3):
                if Player(r, c).type == piece and Player(r+1, c+1).type == piece and Player(r+2, c+2) == piece and Player(r+3, c+3).type == piece:
                    return True

        # Check \ diaganols
        for c in range(self.COLUMN_COUNTS-3):
            for r in range(3, self.ROW_COUNTS):
                if Player(r, c).type == piece and Player(r-1, c+1).type == piece and Player(r-2, c+2).type == piece and Player(r-3, c+3).type == piece:
                    return True

    def game_over(self):
        return self.grid.exists_empty_cells() == False and self.winning_move == False
