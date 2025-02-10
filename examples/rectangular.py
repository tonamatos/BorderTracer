from graph import TilingGraph, Tile
from itertools import product

class RectangularTilingGraph(TilingGraph):
  def __init__(self, cols=10, rows=10, size_x=1, size_y=1):
    super().__init__()
    self.size_x = size_x
    self.size_y = size_y
    tiles = self._create_rectangular_tiling(cols, rows, size_x, size_y)
    self.add_nodes_from(tiles)
    self.orientation = {}

  def create_adjacencies(self, adjacency="4-adj"):
    if adjacency   == "4-adj": self._create_4adjacencies()
    elif adjacency == "8-adj": self._create_8adjacencies()
    else:
      raise NotImplementedError("Unkown adjacency.")

  def _create_rectangular_tiling(self, cols, rows, size_x, size_y):
    '''
    Creates the set of all tiles in a rectangular grid.
    '''
    tiles = set()
    for n, m in product(range(cols), range(rows)):
      x, y = n*size_x, m*size_y
      vertices = [(x, y),
                  (x + size_x, y),
                  (x + size_x, y + size_y),
                  (x, y + size_y)]
      
      center   = (x + size_x/2, y + size_y/2)
      
      tiles.add(Tile(vertices, center))

    return tiles
    
  def _create_4adjacencies(self):
    directions = {'right': (self.size_x, 0),
                  'up'   : (0, self.size_y),
                  'left' : (-self.size_x, 0),
                  'down' : (0, -self.size_y)}
    
    self._create_adjacencies_from_direction(directions)

  def _create_8adjacencies(self):
    directions = {'right'    : (self.size_x, 0),
                  'upright'  : (self.size_x, self.size_y),
                  'up'       : (0, self.size_y),
                  'upleft'   : (-self.size_x, self.size_y),
                  'left'     : (-self.size_x, 0),
                  'downleft' : (-self.size_x, -self.size_y),
                  'down'     : (0, -self.size_y),
                  'downright': (self.size_x, -self.size_y)}
    
    self._create_adjacencies_from_direction(directions)
