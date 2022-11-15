from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
import mesa

from model import PlayerModel

NUMBER_OF_CELLS = 42
SIZE_OF_CANVAS_IN_PIXEL_X = 6
SIZE_OF_CANVAS_IN_PIXEL_Y = 7


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(PlayerModel,
                                          [grid],
                                          "My Model",
                                          {'n_agents': 10})
server.launch()
