import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_tiling(tiling_graph, draw_adjacencies=False):
  # Get bounding box of all tiles
  min_x = min(tile.center[0] for tile in tiling_graph.nodes) - 1
  max_x = max(tile.center[0] for tile in tiling_graph.nodes) + 1
  min_y = min(tile.center[1] for tile in tiling_graph.nodes) - 1
  max_y = max(tile.center[1] for tile in tiling_graph.nodes) + 1
    
  # Dynamically adjust figure size
  width, height = max_x - min_x, max_y - min_y
  fig, ax = plt.subplots(figsize=(width / 2, height / 2))

  for tile in tiling_graph.nodes:
    # Extract tile color and vertices
    color = getattr(tile, "color", "lightgray")
    polygon = patches.Polygon(tile.vertices, edgecolor="black", facecolor=color, alpha=0.6)
    ax.add_patch(polygon)

    if draw_adjacencies:
      # Draw tile center
      x, y = tile.center
      ax.plot(x, y, "ro", markersize=1)

  if draw_adjacencies:
    for tile in tiling_graph.nodes:
      for neighbor in tiling_graph.successors(tile):
        x1, y1 = tile.center
        x2, y2 = neighbor.center
        ax.plot([x1, x2], [y1, y2], "r-", linewidth=0.5)

  ax.set_aspect('equal')
  ax.set_xlim(min_x, max_x)
  ax.set_ylim(min_y, max_y)
  ax.invert_yaxis()

  # Remove axes for a clean look
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_frame_on(False)

  plt.show()

