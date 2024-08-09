from classes import Tile, Cell
import glob


grid_width = 4
grid_height = 4

# Create Tile Objects
tiles = []
names = ["up", "right", "down", "left", "all", 
         "right_end", "down_end", "left_end", "up_end", "blank"]

cells = []

for num, file in enumerate(glob.glob("images/*.jpg")):
    tile = Tile(file, names[num])
    tiles.append(tile)

for i in range(grid_width * grid_height):
    cell = Cell(i)
    cells.append(cell)