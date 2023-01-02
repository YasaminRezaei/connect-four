"""
Generalized behavior for random walking, one grid cell at a time.
"""

import mesa


class Rules(mesa.Agent):
    """
    Class implementing random walker methods in a generalized manner.

    Not intended to be used on its own, but to inherit its methods to multiple
    other agents.
    """
    grid = None
    x = None
    y = None
    moore = True

    def __init__(self, unique_id, pos, model, moore=True):
        """
        grid: The SingleGrid object in which the agent lives.
        x: The agent's current x coordinate
        y: The agent's current y coordinate
        moore: If True, may move in all 8 directions.
                Otherwise, only up, down, left, right.
        """
        super().__init__(unique_id, model)
        self.pos = pos
        self.moore = moore

    def random_move(self):
        """
        Step one cell in any allowable direction.
        """
        # ich lasse hier auscommentiert. damit sich nicht bewegen.
        # Pick the next cell from the adjacent cells.
        # next_moves = self.model.grid.get_neighborhood(
        #     self.pos, self.moore, True)
        # next_move = self.random.choice(next_moves)
        # # Now move:
        # self.model.grid.move_agent(self, next_move)

    def get_next_open_row(self, column):
        for row in range(self.ROW_COUNT):
            if self.model.grid.is_cell_empty((column, row)):
                return row

    def is_valid_location(self, column):
        return self.model.grid.is_cell_empty((column, self.ROW_COUNT-1))

    def winning_move(self, turn):
        # Check horizontal locations for win
        for r in range(self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT-3):
                if self.model.grid[c][r] and self.model.grid[c+1][r] and self.model.grid[c+2][r] and self.model.grid[c+3][r]:
                    if self.model.grid[c][r].type == turn and self.model.grid[c+1][r].type == turn and self.model.grid[c+2][r].type == turn and self.model.grid[c+3][r].type == turn:
                        return True

        # Check vertical locations for win ?????
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT):
                if self.model.grid[c][r] and self.model.grid[c][r+1] and self.model.grid[c][r+2] and self.model.grid[c][r+3]:

                    if self.model.grid[c][r].type == turn and self.model.grid[c][r+1].type == turn and self.model.grid[c][r+2].type == turn and self.model.grid[c][r+3].type == turn:
                        print('turn')
                        return True

        # Check positively sloped diaganols /
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT-3):
                if self.model.grid[c][r] and self.model.grid[c+1][r+1] and self.model.grid[c+2][r+2] and self.model.grid[c+3][r+3]:
                    if self.model.grid[c][r].type == turn and self.model.grid[c+1][r+1].type == turn and self.model.grid[c+2][r+2].type == turn and self.model.grid[c+3][r+3].type == turn:
                        return True

        # Check negatively sloped diaganols \
        for r in range(3, self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT-3):
                if self.model.grid[c][r] and self.model.grid[c+1][r-1] and self.model.grid[c+2][r-2] and self.model.grid[c+3][r-3]:
                    if self.model.grid[c][r].type == turn and self.model.grid[c+1][r-1].type == turn and self.model.grid[c+2][r-2].type == turn and self.model.grid[c+3][r-3].type == turn:
                        return True

    def game_over(self, turn):
        return self.winning_move(turn) or not self.model.grid.exists_empty_cells()
