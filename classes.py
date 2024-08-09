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
    
    
    
