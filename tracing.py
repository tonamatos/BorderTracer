class BorderTracingError(Exception):
  '''
  Custom exception for errors in border tracing.
  '''
  pass

class BorderTracer:
  def __init__(self, tiling_graph, object_C):
    '''
    Initializes the BorderTracer with a given tiling graph.
        
    Args:
      tiling_graph (graph.TilingGraph): A graph representing the tiling.
      object_C (set): A set of tiles fully surrounded by the tiling_graph nodes.
    '''
    self.tiling_graph = tiling_graph
    self.object_C     = object_C
    self.border_tiles = []

  def __str__(self):
    string = ''
    for tile in self.border_tiles:
      string = string+str(tile)+'\n'
    return string

  def trace_border(self, start_node=None):
    '''
    Traces the border of the tiling by finding the ordered list of border tiles.
        
    Args:
      start_node (optional): The node to start the border tracing from. If None,
      it will find a border node using _find_border_start(self).
        
    Returns:
      List of nodes representing the border in order.
    '''
    if start_node is None:
      # Find a border node to start the tracing
      start_node, neighbor_q = self._find_border_start()

    self._trace_from_node(start_node, neighbor_q)
    return self.border_tiles

  def _find_border_start(self):
    '''
    Finds a border node to start tracing.

    Returns:
      A node on the border to start the trace and its neighbor.
    '''
    for tile_t in self.object_C:
      for neighbor_q in self.tiling_graph.neighbors(tile_t):
        if neighbor_q not in self.object_C:
          return tile_t, neighbor_q

    raise BorderTracingError("No border nodes found. The input object might be empty or improperly defined.")
      
  def _find_next_contour_tile(self, b):
    '''
    Performs Steps 2 and 3 of Algorithm 2. I.e. assumes two tiles are already in
    self.border_tiles, which determine the direction of the tracing.
    Returns the next border tile (does not get added to the list,
    since the algorithm needs to check for end condition before that.)
    '''
    orientation = self.tiling_graph.orientation
    current_tile = self.border_tiles[-1]
    k = len(orientation[current_tile])

    for _ in range(k):
      b = (b + 1) % k  # Increment Freeman code direction
      next_tile = orientation[current_tile][b]  # Get corresponding tile

      if next_tile in self.object_C:  # Found first object tile
        return next_tile
    
    raise BorderTracingError(f"Tracing stuck at {current_tile}.")

  def _trace_from_node(self, start_node, neighbor_q):
    '''
    Traces the border starting from a specific node.

    Args:
      start_node: The starting node for the trace.
      neighbor_q: A neighbor of start_node that is in (N \ C).
        
    Returns:
      List of nodes representing the border tiles in order.
    
    Raises:
      ValueError: If no border mesh exists (e.g., C is an isolated tile).
    '''
    # STEP 1 of Algorithm 2 
    self.border_tiles = [start_node]
    G = self.tiling_graph
    f = G.create_freeman_code()

    # STEP 2 of Algorithm 2
    b = f(start_node, neighbor_q)  # Get Freeman code direction
    next_tile = self._find_next_contour_tile(b)
    self.border_tiles.append(next_tile)

    # STEP 3 of Algorithm 2
    while True:
      current_tile  = self.border_tiles[-1]
      previous_tile = self.border_tiles[-2]
      b = f(current_tile, previous_tile)
      next_tile = self._find_next_contour_tile(b)
      if next_tile != start_node:
        self.border_tiles.append(next_tile)
        continue
      else:
        self.border_tiles.append(next_tile)
        current_tile  = self.border_tiles[-1]
        previous_tile = self.border_tiles[-2]
        b = f(current_tile, previous_tile)
        next_tile = self._find_next_contour_tile(b)
        if next_tile == self.border_tiles[1]:
          self.border_tiles.pop()
          return
        else:
          self.border_tiles.append(next_tile)
          continue

    