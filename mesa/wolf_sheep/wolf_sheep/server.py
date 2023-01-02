import mesa

from wolf_sheep.agents import Wolf, Sheep
from wolf_sheep.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Sheep:
        portrayal["Shape"] = "circle"
        portrayal["r"] = " 0.5"
        portrayal["Color"] = "#FF3232"
        portrayal["Filled"] = "#true"

        portrayal["scale"] = 0.5
        portrayal["Layer"] = 1

    elif type(agent) is Wolf:
        portrayal["Shape"] = "circle"
        portrayal["r"] = " 0.5"
        portrayal["Color"] = "#191919"
        portrayal["Filled"] = "true"
        portrayal["scale"] = 0.5
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    wolf_sheep_portrayal, 10, 10, 500, 500)
chart_element = mesa.visualization.ChartModule(
    [
        {"Label": "Wolves", "Color": "#AA0000"},
        {"Label": "Sheep", "Color": "#666666"},

    ]
)

model_params = {
    # The following line is an example to showcase StaticText.
    "title": mesa.visualization.StaticText("Parameters:"),


    "initial_sheep": mesa.visualization.Slider(
        "Initial Sheep Population", 100, 10, 300
    )

}

server = mesa.visualization.ModularServer(
    WolfSheep, [canvas_element,
                chart_element], "Wolf Sheep Predation", model_params
)
server.port = 8521
