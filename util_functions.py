def find_movement_direction(start_coord, end_coord):
  """
  Determines the direction of movement between two adjacent cells on a 2D grid.

  Args:
    start_coord: A tuple representing the (x, y) coordinates of the starting cell.
    end_coord: A tuple representing the (x, y) coordinates of the ending cell.

  Returns:
    A string indicating the direction of movement ('North', 'South', 'East', 'West', or 'No Movement' if the cells are not adjacent), or None if the input is invalid.
  """

  x1, y1 = start_coord
  x2, y2 = end_coord

  x_diff = x2 - x1
  y_diff = y2 - y1

  if abs(x_diff) + abs(y_diff) != 1:
    return "No Movement"  # Cells are not adjacent

  if x_diff == 0:
    if y_diff == 1:
      return "North"
    elif y_diff == -1:
      return "South"
  elif y_diff == 0:
    if x_diff == 1:
      return "East"
    elif x_diff == -1:
      return "West"

  return None # Should not reach here if cells are adjacent

def find_turns_using_functions(start_orientation, end_orientation):
  """
  Determines the sequence of TurnRight or TurnLeft operations to go from a
  starting orientation to an ending orientation.

  Args:
    start_orientation: A string representing the initial orientation.
    end_orientation: A string representing the target orientation.

  Returns:
    A list of strings, where each string is either 'TurnRight()' or 'TurnLeft()',
    or None if the input orientations are invalid.
  """
  orientations = ['North', 'East', 'South', 'West']
  start_index = orientations.index(start_orientation)
  end_index = orientations.index(end_orientation)

  turns = []

  # Check clockwise (right turns)
  clockwise_diff = (end_index - start_index) % 4
  if clockwise_diff <= 2:
    turns.extend(['TurnRight'] * clockwise_diff)
    return turns
  else:
    # Check counter-clockwise (left turns)
    counter_clockwise_diff = (start_index - end_index) % 4
    turns.extend(['TurnLeft'] * counter_clockwise_diff)
    return turns
