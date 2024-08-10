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

    def __repr__(self):
        return f'{self.name}: {self.path}'
    
    def __str__(self):
        return f'{self.name}: {self.path}'

# Cells positioned on grid to hold tile objects
class Cell:
    def __init__(self, position):
        self.position = position
        self.tile = None
        self.options = TILES_NUM

    def __repr__(self):
        return f'{self.position} ({self.tile})'    
