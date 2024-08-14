import pandas as pd
import random

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
        self.weight = None

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name.upper()

    def tile_data_process(tile_list):
        for index, tile in enumerate(tile_list):
            edges = TILES_DF.loc[TILES_DF['index'] == index + 1, 
                                 ['up_edge', 'right_edge', 'down_edge', 'left_edge']].values.flatten()
            tile.edges = edges.tolist()
            weight = TILES_DF.loc[TILES_DF['index'] == index + 1, ['weightage']].squeeze()
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
        self.entropy = len(self.options)
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

    def cell_options(self, cells_list):
        if self.cell_up(cells_list).tile:
            tile_up = self.cell_up(cells_list).tile
            up_options = tile_up.down
        if self.cell_right(cells_list.tile):
            tile_right = self.cell_up(cells_list).tile
            right_options = tile_right.left
        if self.cell_down(cells_list):
            tile_down = self.cell_down(cells_list).tile
            down_options = tile_down.up
        if self.cell_left(cells_list):
            tile_left = self.cell_left(cells_list).tile
            left_options = tile_left.right
        options = list_intersection([up_options, right_options, down_options, left_options,], 1)
        self.options = options

    def pick_tile(self):
        weights = TILES_DF['weightage'].to_list()
        self.tile = random.choices(self.options, weights=weights)