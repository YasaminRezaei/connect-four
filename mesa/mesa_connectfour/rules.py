import mesa


class Rules(mesa.Agent):

    def __init__(self, width=GRIDWIDTH, height=GRIDHEIGHT, connnect=4):
        self.game_over = False

    def is_valid_location(self):
        pass
    def winning_move(self):
        pass
