from classes import Tile
import glob

# Create Tile Objects
tiles = []
names = ["up", "right", "down", "left", "all", 
         "right_end", "down_end", "left_end", "up_end", "blank"]

for num, file in enumerate(glob.glob("images/*.jpg")):
    tile = Tile(file, names[num])
    tiles.append(tile)

print(tiles)