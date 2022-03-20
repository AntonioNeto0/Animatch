import pandas as pd


class Handler:
    def __init__(self):
        self.ds = pd.read_csv("resources_dataset/dataset/Anime.csv")
        # Trocar o nome da season Fall para Autums na coluna Release_season
        self.replace_names('Release_season', 'Fall ', 'Autumn')

# Fxtion
    def replace_names(self, column, oldValue, newValue):
        self.ds[column].replace([oldValue], newValue, inplace=True)
