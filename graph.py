import networkx as nx

class Tile:
  def __init__(self, vertices, center, color=None, type=None):
    self.vertices = vertices
    self.center   = center
    if color:
      self.color  = color
    if type:
      self.type = type
    
  def __str__(self): return str(self.center)
  def __hash__(self): return hash(self.center)
  def __eq__(self, other): return self.center == other.center

class TilingGraph(nx.DiGraph):
  '''
  A subclass of networkx.DiGraph that represents a tiling with oriented adjacency.
  Each node has neighbors ordered by their orientation.
  '''
  def __init__(self):
    super().__init__()
    self.orientation = {}
  
  def highlight(self, tile_centers, color='skyblue'):
    '''
    Changes the color of the tiles corresponding to the given tile_centers
    to distinguish them from the background.
    '''
    for tile in self.nodes():
      if tile.center in tile_centers:
        tile.color = color

  def create_freeman_code(self):
    '''
    Creates a function that assigns Freeman chain codes based on `self.orientation`.
    
    Returns:
      function: A function f(i, j) that returns the Freeman code for edge (i, j).
    '''
    def freeman_code(tile1, tile2):
      if tile1 not in self.orientation:
        raise ValueError(f"Tile {tile1} is not in the orientation dictionary.")
            
      if tile2 not in self.orientation[tile1]:
        raise ValueError(f"Tiles {tile1} and {tile1} are not adjacent in the orientation.")
      
      return self.orientation[tile1].index(tile2)
      
    return freeman_code
  
  def _create_adjacencies_from_direction(self, directions, filter=None):
    '''
    Fills self.orentation with correct order of neighbors for each
    node. Also adds all edges depending on the directions dictionary.
    filter allows to determine a tile_type so that it will only affect
    those tiles with that type. If left blank, all tiles are treated.
    Useful for when tiles may have different orientations, needing
    different sets of directions.
    '''
    existing_centers = {tile.center : tile for tile in self.nodes()}

    if filter is None:
      tiles_to_update = self.nodes()
    else:
      tiles_to_update = [tile for tile in self.nodes() if tile.type == filter]

    for tile in tiles_to_update:
      tile_orientation = []
      for direction in directions.values():
        center_from = tile.center
        x, y = direction
        center_to = (center_from[0] + x, center_from[1] + y)
        if center_to in existing_centers.keys():
          other_tile = existing_centers[center_to]
          # Add arc to DiGraph:
          tile_orientation.append(other_tile)
          self.add_edge(tile, other_tile)
      
      # Update tile orientation
      self.orientation[tile] = tuple(tile_orientation)