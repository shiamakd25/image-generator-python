from classes import Tile, Cell
import glob
import random

from config import *

# Create Tile Objects
tiles = []
names = ["up", "right", "down", "left", "all", 
         "right_end", "down_end", "left_end", "up_end", "blank"]

cells = []

for num, file in enumerate(glob.glob("images/*.jpg")):
    tile = Tile(file, names[num-1])
    tiles.append(tile)

for i in range(GRID_WIDTH * GRID_HEIGHT):
    cell = Cell(i)
    cells.append(cell)