import mesa
from random_move import RandomWalker


class Board(mesa.Agent):
    def __init__(self, unique_id, model):
        # initialize the parent class with required parameters
        super().__init__(unique_id, model)

    def evaluat_board(Rules):
        print("evaluate")


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
        # move to a cell in my Moore neighborhood
        self.random_move()
     

        self.board.evaluat_board()
