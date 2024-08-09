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
        return self.name
    
    def __str__(self):
        return self.name

# Cells positioned on grid to hold tile objects
class Cell:
    def __init__(self, position):
        self.position = position
        self.tile = None

    def __repr__(self) -> str:
        return f'{self.position} ({self.tile})'    
