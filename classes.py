import pandas as pd

from config import *

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
        self.weight = None

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name.upper()

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
            weight = df.loc[df['index'] == index + 1, ['weightage']].squeeze()
            tile.weight = weight
    
    def compare_tiles(self, tiles_list):
        for tile in tiles_list:
            if self.edges[0] == tile.edges[2]:
                self.up.append(tile)
            if self.edges[1] == tile.edges[3]:
                self.right.append(tile)
            if self.edges[2] == tile.edges[0]:
                self.down.append(tile)
            if self.edges[3] == tile.edges[1]:
                self.left.append(tile)

# Cells positioned on grid to hold tile objects
class Cell:
    def __init__(self, position):
        self.position = position
        self.tile = None
        self.options = TILES_NUM
        self.collapsed = False

    def __repr__(self):
        return f'{self.position} ({self.tile})'
    
    def cell_up(self, cells_list):
        cell_up = None
        if self.position > GRID_WIDTH:
            position = self.position - GRID_WIDTH
            for cell in cells_list:
                if cell.position == position:
                    cell_up = cell
        return cell_up
    
    def cell_right(self, cells_list):
        cell_right = None
        invalid_positions = []
        for i in range(GRID_HEIGHT):
            invalid_positions.append(GRID_WIDTH * (i + 1) -1)
        if self.position not in invalid_positions:
            position = self.position - 1
            for cell in cells_list:
                if cell.position == position:
                    cell_right = cell
        return cell_right
    
    def cell_down(self, cells_list):
        cell_down = None
        if self.position < (GRID_WIDTH - 1)  * GRID_HEIGHT:
            position = self.position + GRID_WIDTH
            for cell in cells_list:
                if cell.position == position:
                    cell_down = cell
        return cell_down
    
    def cell_left(self, cells_list):
        cell_left = None
        invalid_positions = []
        for i in range(GRID_HEIGHT):
            invalid_positions.append(GRID_WIDTH * i)
        if self.position not in invalid_positions:
            position = self.position - 1
            for cell in cells_list:
                if cell.position == position:
                    cell_left = cell
        return cell_left
    
    def check_collapsed(self):
        if self.options == 1:
            self.collapsed = True
        else:
            self.collapsed = False

    def cell_options(self):
        options = None
        self.options = options