import random
import mesa

from agents import Board, Player
from rules import Rules


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

    ROW_COUNTS = 6
    COLUMN_COUNTS = 7
    # turn wird jedes mal gewechselt
    PLAYER1 = 0
    PLAYER2 = 1
    #turn = random.randint(PLAYER1, PLAYER2)

    def __init__(self, width=GRIDWIDTH, height=GRIDHEIGHT, connnect=4):

        self.width = width
        self.height = height

        self.connnect = connnect

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width, height, torus=True)
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

        self.creat_players()

        # create a single board for the model
        self.board = Board(1, self)

    def creat_players(self):
        self.board = Board(1, self)
        for i in range(0, 5):
            if self.turn == 0:
                print(i, "if")
                print(self.turn)
                column = random.randrange(0, 5)
                #column = 3
                print("colomn", column)
                if Rules.is_valid_location(self, column):
                    row = self.board.get_next_open_row(column)
                    print("row", row)
                    player = self.board.drop_piece(i, row, column, 1)
                    self.grid.place_agent(player, (row, column))
                    # self.schedule.add(player)

                self.turn += 1
                self.turn = self.turn % 2

            else:
                print(i, "elif")
                print(self.turn)
                column = random.randrange(0, 5)  # 0-6
                print("colomn", column)
                if Rules.is_valid_location(self, column):
                    row = self.board.get_next_open_row(column)
                    print("row", row)
                    player = self.board.drop_piece(i, row, column, 2)
                    self.grid.place_agent(player, (row, column))
                    self.schedule.add(player)
                # # add the Person object to the model schedul
                # self.schedule.add(player2)

                self.turn += 1
                self.turn = self.turn % 2
        # self.schedule.add(player)
        self.running = True
        print(Rules.game_over(self))

    def step(self):
        print("step model")
        # tell all the agents in the model to run their step function

        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run_model(self):

        print("run model")
        self.step()
