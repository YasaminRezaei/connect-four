import random
import mesa
from connect_four.rules import Rules


class Player(Rules):
    """
    The init is the same as the Rules.
    """

    type = None
    ROW_COUNT = 6
    COLUMN_COUNT = 7

    def __init__(self, unique_id, pos, model, moore, type=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.type = type
        self.turn = not self.type  # wenn rot dann gelb oder umgekehr

    def step(self):
        print("step agent")
        """
        A model step.
        """
        # hier wird pro step ein Agent produziert. drop piece
        # danach wird turn jedesmal geändert
        self.game_over(self.turn)
        if (not self.game_over(self.turn)):
            if (self.model.grid.find_empty()):
                column = self.random.randrange(self.model.width)
                if self.is_valid_location(column):
                    row = self.get_next_open_row(column)
                    player = Player(
                        self.model.next_id(), self.pos, self.model, self.moore, self.turn
                    )
                    self.model.grid.place_agent(player, (column, row))
                    if self.winning_move(self.turn):
                        print(self.turn, "gewonnen")
                    self.turn += 1
                    self.turn = self.turn % 2
