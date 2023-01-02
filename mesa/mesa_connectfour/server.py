import mesa

from model import ConnectFour
from agents import Player

RED = "#cc2b12"
YELLOW = "#e8f00c"


def get_players_agents(model):
    """
    Display a text count of how many happy agents there are.
    """
    return f"player1 agents: {model.datacollector} player2 agents: {model.datacollector}"


def player_portrayal(agent):

    if agent is None:
        return

    portrayal = {}

    if isinstance(agent, Player):

        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.5
        portrayal["Layer"] = 0
        portrayal["Filled"] = "true"
        color = RED

        # set agent color based on savings and loans
        if agent.type == 1:
            color = YELLOW
        if agent.type == 2:
            color = RED

        portrayal["Color"] = color
    return portrayal


# def get_red_agents(model):
#     """
#     Display a text count of how many red Piece there are.
#     """
#     return f"red Piece: {model.PLAYER_PIECE1}  yellow Piece: {model.PLAYER_PIECE2}"


# def agent_portrayal(agent):
#     """
#     Portrayal Method for canvas
#     """
#     portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

#     if agent.agent_type == 1:
#         portrayal["Color"] = ["#FF0000", "#FF9999"]
#         portrayal["stroke_color"] = "#00FF00"
#     elif agent.agent_type == 2:
#         portrayal["Color"] = ["#faee07", "#f7f79e"]
#         portrayal["stroke_color"] = "#000000"
#     elif agent.agent_type == 0:
#         portrayal["Color"] = ["#eeeeee", "#f7f79e"]
#         portrayal["stroke_color"] = "#000000"
#     else:
#         return


grid = mesa.visualization.CanvasGrid(
    player_portrayal, 7, 6, 500, 500)
chart = mesa.visualization.ChartModule(
    [{"Label": "red", "Color": RED},
     {"Label": "yello", "Color": YELLOW},

     ])

model_params = {
    "height": 6,
    "width": 7,
    "connnect": mesa.visualization.Slider("Connect 4", 2, 0, 4, 1),
}

server = mesa.visualization.ModularServer(
    ConnectFour,
    [grid, get_players_agents, chart],
    "Connect 4",
    model_params,
)
