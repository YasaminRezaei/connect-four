import mesa

from connect_four.agents import Player
from connect_four.model import ConnectFour


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if agent.type == 1:
        portrayal["Shape"] = "circle"
        portrayal["r"] = " 0.5"
        portrayal["Color"] = "#FF3232"
        portrayal["Filled"] = "#true"
        portrayal["Layer"] = 1
    elif agent.type == 0:
        portrayal["Shape"] = "circle"
        portrayal["r"] = " 0.5"
        portrayal["Color"] = "#FFFF00"
        portrayal["Filled"] = "#true"
        portrayal["Layer"] = 1

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    wolf_sheep_portrayal, 7, 6, 500, 500)
chart_element = mesa.visualization.ChartModule(
    [

        {"Label": "Player", "Color": "#666666"},

    ]
)

model_params = {
    # The following line is an example to showcase StaticText.
    "title": mesa.visualization.StaticText("Parameters:"),



}

server = mesa.visualization.ModularServer(
    ConnectFour, [canvas_element,
                  chart_element], "Wolf Sheep Predation", model_params
)
server.port = 8521
