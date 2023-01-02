import mesa
import random
from connect_four.scheduler import RandomActivationByTypeFiltered
from connect_four.agents import Player

class ConnectFour(mesa.Model):

    height = 10
    width = 10
    verbose = False  # Print-monitoring

    description = (
        "A model for simulating wolf and sheep (predator-prey) ecosystem modelling."
    )

    def __init__(
        self,
        width=7,
        height=6,
  
    ):
      
        super().__init__()
        # Set parameters
        self.width = width
        self.height = height
       
        self.schedule = RandomActivationByTypeFiltered(self)
        self.grid = mesa.space.SingleGrid(self.width, self.height, torus=True)
        self.datacollector = mesa.DataCollector(
            {

                "Player": lambda m: m.schedule.get_type_count(Player)


            }
        )

       # in ja yek bar ejra mishavad.mitavan baraye harkate avalie azash estefade kard.

        column = self.random.randrange(self.width)
        type = random.randint(0, 1)
        player = Player(self.next_id(), (column, 0), self, True, type)

        self.grid.place_agent(player, (column, 0))
        self.schedule.add(player)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        print("step model")

        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.verbose:
            print(
                [
                    self.schedule.time,

                    self.schedule.get_type_count(Player),

                ]
            )

    def run_model(self, step_count=200):

        if self.verbose:

            print("Initial number player: ",
                  self.schedule.get_type_count(Player))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print("")

            print("Final number player: ", self.schedule.get_type_count(Player))
