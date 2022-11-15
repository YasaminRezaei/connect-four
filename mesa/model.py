from mesa import Agent, Model
import mesa
import random

from agent import PlayerAgent
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector


class PlayerModel(Model):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        #self.minority_pc = minority_pc
        #self.homophily = homophily

        
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(height, width, torus=True)

        

        self.running = True

        # Set up agents
        # We use a grid iterator that returns
        # the coordinates of a cell as well as
        # its contents. (coord_iter)
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            # ---------------------
            agent_type = 1

        agent = PlayerAgent((x, y), self, agent_type)
        self.grid.position_agent(agent, (x, y))
        self.schedule.add(agent)

        def step(self):
            self.game_over = 0
            # while game over----
            while not self.game_over:
               
