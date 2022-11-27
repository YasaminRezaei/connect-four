import random
import mesa

from agents import Board, Player


def get_num_player1_piece(model):
    player1 = [a for a in model.schedule.agents if a.type == 1]
    return len(player1)


def get_num_player2_piece(model):
    player2 = [a for a in model.schedule.agents if a.type == 2]
    return len(player2)


def get_player1_score(model):
    pass


def get_player2_score(model):
    pass


class ConnectFour(mesa.Model):
    # anzahl von rows und columns
    GRIDHEIGHT = 6
    GRIDWIDTH = 7
    # turn wird jedes mal gewechselt
    PLAYER1 = 0
    PLAYER2 = 1
    #turn = random.randint(PLAYER1, PLAYER2)

    def __init__(self, width=GRIDWIDTH, height=GRIDHEIGHT, connnect=4):

        self.width = width
        self.height = height

        self.connnect = connnect

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=True)
        self.turn = random.randint(0, 1)
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "player1": get_num_player1_piece,
                "player2": get_num_player2_piece,
                "player1Score": get_player1_score,
                "player2Score": get_player2_score,

            },
            agent_reporters={"type": lambda x: x.type},
        )

        # create a single board for the model
        self.board = Board(1, self)

        # create player for the model according to number of players set by user
        for i in range(0, 42):
            if self.turn == 0:
                # set x, y coords randomly within the grid
                x = self.random.randrange(self.width)
                y = self.random.randrange(self.height)
                player1 = Player(i, (x, y), self, True, self.board, type=1)
                # place the Person object on the grid at coordinates (x, y)
                if (self.grid.is_cell_empty((x, y))):
                    self.grid.place_agent(player1, (x, y))
                # add the Person object to the model schedule
                # self.schedule.add(player1)

            if self.turn == 1:
                # set x, y coords randomly within the grid
                x = self.random.randrange(self.width)
                y = self.random.randrange(self.height)
                player2 = Player(i, (x, y), self, True, self.board, type=2)
                # place the Person object on the grid at coordinates (x, y)
                if (self.grid.is_cell_empty((x, y))):
                    self.grid.place_agent(player2, (x, y))
                # add the Person object to the model schedule
                # self.schedule.add(player2)

            self.turn += 1
            self.turn = self.turn % 2

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        # tell all the agents in the model to run their step function
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run_model(self):
        for i in range(self.run_time):
            self.step()
