class Node:
  def __init__(self, position, parent=None):
    self.position = position
    self.parent = parent
    self.g = 0  # Cost from start to current node
    self.h = 0  # Heuristic estimate of cost to goal
    self.f = 0  # Total cost (g + h)

def manhattan_distance(a, b):
  # Heuristic function using Manhattan distance
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
  rows, cols = len(grid), len(grid[0])
  open_set = []
  closed_set = set()

  start_node = Node(start)
  open_set.append(start_node)

  while open_set:
    current = min(open_set, key=lambda node: node.f)
    open_set.remove(current)
    closed_set.add(current.position)

    if current.position == goal:
      path = []
      while current:
        path.append(current.position)
        current = current.parent
      return path[::-1]  # Reverse path for start to goal

    for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      new_position = (current.position[0] + delta_row, current.position[1] + delta_col)
      if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols and grid[new_position[0]][new_position[1]] != 1:  # Check for walls
        if new_position in closed_set:
          continue

        parent = current
        g = current.g + 1  # Movement cost (adjust if needed)
        h = manhattan_distance(new_position, goal)
        f = g + h

        new_node = Node(new_position, parent)
        new_node.g = g
        new_node.h = h
        new_node.f = f

        if new_node not in [node for node in open_set if node.position == new_position and node.f >= f]:
          open_set.append(new_node)

  return None  # No path found

# Example usage
grid = [
  [0, 0, 1, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 0],
]

start = (0, 0)
goal = (3, 3)

path = a_star(grid, start, goal)

if path:
  print("Path found:", path)
else:
  print("No path found")