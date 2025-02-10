def circular_object(tiling_graph, center, radius):
  """
  Generates a circular shape in the tiling.
  """
  object_C = {tile for tile in tiling_graph.nodes if 
              ((tile.center[0] - center[0])**2 + (tile.center[1] - center[1])**2) <= radius**2}
  
  return object_C