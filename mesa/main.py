from model import PlayerModel

model = PlayerModel(5)
# data collector
for t in range(10):
    model.step()
model_df = model.dc.get_model_vars_dataframe()
agent_df = model.dc.get_agent_vars_dataframe()
