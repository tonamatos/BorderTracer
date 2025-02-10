from graph import TilingGraph, Tile
from itertools import product

class HexagonalTilingGraph(TilingGraph):
  def __init__(self, cols=10, rows=10, side_length=1):
    super().__init__()
    self.side_length = side_length
    self.hex_height = 3*side_length/2
    tiles = self._create_hexagonal_tiling(cols, rows)
    self.add_nodes_from(tiles)
    self.orientation = {}

  def create_adjacencies(self, adjacency="6-adj"):
    if adjacency == "6-adj": self._create_6adjacencies()
    else:
      raise NotImplementedError("Unkown adjacency.")

  def _create_hexagonal_tiling(self, cols, rows):
    '''
    Creates the set of all tiles in a hexagonal grid.

    Args:
      cols: Number of hexagons in the horizontal direction.
      rows: Number of hexagons in the vertical direction.

    Returns:
      A set of Tile objects representing the hexagonal tiling.
    '''
    # Compute hexagon height and width
    side_length = self.side_length
    hex_height  = self.hex_height
    vert_offset = hex_height/2  # Vertical offset for odd columns
    
    tiles = set()
    for row, col in product(range(rows), range(cols)):
      x = col * 2 * side_length  # Horizontal spacing
      y = row * (3/2) * side_length  # Vertical spacing

      # Shift every odd row to the right by half a hexagon
      if row % 2 == 1:
        x += side_length  # Shift right

      # Define hexagon vertices (counterclockwise order)
      vertices = [(x, y - side_length),                  # Top
                  (x + side_length, y - side_length / 2),  # Top-right
                  (x + side_length, y + side_length / 2),  # Bottom-right
                  (x, y + side_length),                  # Bottom
                  (x - side_length, y + side_length / 2),  # Bottom-left
                  (x - side_length, y - side_length / 2)]  # Top-left

      tiles.add(Tile(center=(x, y), vertices=vertices))


    return tiles
    
  def _create_6adjacencies(self):
    length = self.side_length
    directions = {'right'     : (2*length, 0),
                  'upright'   : (length, length * 3/2),
                  'upleft'    : (-length, length * 3/2),
                  'left'      : (-2*length, 0),
                  'downleft'  : (-length, -length * 3/2),
                  'downright' : (length, -length * 3/2)}
    
    self._create_adjacencies_from_direction(directions)