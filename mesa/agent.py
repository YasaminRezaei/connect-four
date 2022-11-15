from mesa import Agent, Model


class PlayerAgent(Agent):
    def __init__(self, pos, model, agent_type):
        super().__init__(pos, model)
        # type 0 or 1 um zu sehen, welche nachbarn gibt.
        self.pos = pos
        self.type = agent_type

    def step(self):
        # Was der Agent tut, wenn er aktiviert wird
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1
                print(similar)
