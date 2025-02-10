from graph import TilingGraph, Tile
from itertools import product

class TriangularTilingGraph(TilingGraph):
  def __init__(self, cols=10, rows=10, side_length=1):
    super().__init__()
    self.side_length = side_length
    self.height = side_length # Warning: irrational numbers might produce rounding errors!
    tiles = self._create_triangular_tiling(cols, rows)
    self.add_nodes_from(tiles)
    self.orientation = {}

  def create_adjacencies(self, adjacency="3-adj"):
    if adjacency   == "3-adj": self._create_3adjacencies()
    else:
      raise NotImplementedError("Unkown adjacency.")

  def _create_triangular_tiling(self, cols, rows):
    '''
    Creates the set of all tiles in a triangular grid.
    '''
    # Compute triangle height (using 60-degree angles)
    height      = self.height
    side_length = self.side_length
    tiles = set()

    for n, m in product(range(rows), range(cols)):
      # Determine if the triangle is pointing up or down
      is_upward = (n + m) % 2 == 0
      
      # Compute center coordinates
      x = m * side_length * 0.5
      y = n * height

      # Define triangle vertices
      if is_upward:
        vertices = [(x, y - height/2), (x - side_length/2, y + height/2), (x + side_length/2, y + height/2)]
        type = 'up'
      else:
        vertices = [(x - side_length/2, y - height/2), (x + side_length/2, y - height/2), (x, y + height/2)]
        type = 'down'
  
      tiles.add(Tile(center=(x, y), vertices=vertices, type=type))

    return tiles
    
  def _create_3adjacencies(self):
    '''
    Must distinguish between triangles that face up and those that
    face down, since they will have different directions.
    '''
    up_directions = {'right': (self.side_length/2, 0),
                      'left': (-self.side_length/2, 0),
                      'down': (0, self.height)}
    
    down_directions = {'right': (self.side_length/2, 0),
                          'up': (0, -self.height),
                        'left': (-self.side_length/2, 0)}
    
    self._create_adjacencies_from_direction(up_directions, filter='up')
    self._create_adjacencies_from_direction(down_directions, filter='down')