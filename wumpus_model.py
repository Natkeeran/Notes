# -*- coding: utf-8 -*-
"""WumpusModel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DMI2YcxqBnfX0OfdldbHLsey8mQr4nG7
"""



from pomegranate.distributions import Categorical
from pomegranate.distributions import ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork
import torch

# Given x and y, get valid adjacent cells in a 4 by 4 grid
def get_wumpus_adjacent_cells(x, y):
        adjacent_cells = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        valid_adjacent_cells = []
        for cell in adjacent_cells:
          if not (cell[0] == 0 or cell[0] == 5 or cell[1] == 0 or cell[1] == 5):
            valid_adjacent_cells.append(cell)
        return valid_adjacent_cells

# For each stench_location, we want to find which wumpus locations influence it
# If they influence it, then probably is [0, 1], if they don't [1, 0]

def get_conditional_probabilities_wumpus(stench_location_x, stench_location_y):

  probs = []
  for x in range(1, 5):
    for y in range(1, 5):
      adjacent_cells = get_wumpus_adjacent_cells(stench_location_x, stench_location_y)
      adjacent_cells.append((stench_location_x, stench_location_y))

      if (x, y) in adjacent_cells:
        prob = [0., 1.]
      else:
        prob = [1., 0.]
      probs.append(prob)
  stench = ConditionalCategorical([probs])
  return stench

# Build a BayesianNetwork to related wumpus location and stench
def get_wumpus_model():
  wumpus = Categorical([[0, 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15., 1./15.]])

  # For each location, get probabilities
  # Build all the stench variables with conditional probabilities
  stench_variables = []
  for x in range(1, 5):
    for y in range(1, 5):
      stench_cond_prob = get_conditional_probabilities_wumpus(x, y)
      stench_variables.append(stench_cond_prob)

  wumpus_variables = [wumpus] + stench_variables
  wumpus_edges = []
  for stench in stench_variables:
    wumpus_edges.append((wumpus, stench))

  wumpus_model = BayesianNetwork(wumpus_variables, wumpus_edges)
  return wumpus_model

# This is a dictionary to track the order of variables and cells
def build_wumpus_tensor_index():
    stench_locations = []
    for x in range(1, 5):
      for y in range(1, 5):
        stench_locations.append("stench_" + str(x) + "_" + str(y))
    return stench_locations

# Agent location as tuple (x, y)
# Agent sense 0 or 1
# Make a prediction based on the model
def get_wumpus_prediction(current_tensor, wumpus_model, agent_location, agent_sense):
  stench_tensor_index = build_wumpus_tensor_index()
  stench_index = stench_tensor_index.index('stench_' + str(agent_location[0]) + "_" + str(agent_location[1]))
  current_tensor[stench_index + 1] = 1

  new_torch_tensor =  [current_tensor]
  X = torch.tensor(new_torch_tensor)

  X_masked = torch.masked.MaskedTensor(X, mask=X >= 0)
  new_wumpus_prediction = wumpus_model.predict_proba(X_masked)
  return new_wumpus_prediction, new_torch_tensor

def get_location_with_best_chance_for_wumpus(prediction):
  prediction_tensor = prediction[0][0]

  max_value_index = None
  current_max_value = 0

  for idx, value in enumerate(prediction_tensor):
    if value > .51 and value > current_max_value:
      max_value_index = idx
  print(max_value_index)

def test_wumbus_model():
  wumpus_model = get_wumpus_model()
  wumpus_tensor = [-1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1,
                 -1, -1, -1, -1, -1,
                 -1, -1
                 ]
  agent_location = (2, 1)
  pre, wumpus_tensor = get_wumpus_prediction(wumpus_tensor, wumpus_model, agent_location, 1)
  print(wumpus_tensor)
  print(pre)

test_wumbus_model()

