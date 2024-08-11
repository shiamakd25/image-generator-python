import pandas as pd

from config import *
from functions import *

# Tile image objects displayed within cells
class Tile:
    def __init__(self, image_path, name):
        self.path = image_path
        self.name = name
        self.edges = []
        self.up = []
        self.right = []
        self.down = []
        self.left = []

    def __repr__(self):
        return f'{self.name}: {self.path}'
    
    def __str__(self):
        return f'{self.name}: {self.path}'

    def tile_data_process(data, tile_list):
        dtypes = {
            'up_edge': str,
            'right_edge': str,
            'down_edge': str,
            'left_edge': str
        }
        df = pd.read_csv(data, dtype=dtypes)
        df.columns = df.columns.str.strip()
        for index, tile in enumerate(tile_list):
            edges = df.loc[df['index'] == index + 1, ['up_edge', 'right_edge', 'down_edge', 'left_edge']].values.flatten()

            tile.edges = edges.tolist()
            print(tile, tile.edges)

# Cells positioned on grid to hold tile objects
class Cell:
    def __init__(self, position):
        self.position = position
        self.tile = None
        self.options = TILES_NUM

    def __repr__(self):
        return f'{self.position} ({self.tile})'    
