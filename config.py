import pandas as pd

GRID_WIDTH = 4
GRID_HEIGHT = 4
TILES_NUM = 10
TILES_DF =  pd.read_csv("tile_config.csv", dtype={'up_edge':str, 'right_edge':str, 'down_edge':str, 'left_edge':str})