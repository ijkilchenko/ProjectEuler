import utilsPrimes as utils
import logging
import numpy as np
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def make_pairs(N):
  """Makes a prime pairs graph and a number of edges dictionary. 
  
  Args:
    N: Largest possibl3 prime in the prime pairs graph.

  Returns:
    A dictionary and a number of edges dictionary (as a tuple).
  """

  g = defaultdict(lambda: [])
  # Maps the number of edges to the list of nodes which have that many edges.
  v = defaultdict(lambda: [])

  for i in range(3, N):
    if not utils.isPrime(i):
      continue
    for j in range(i+1, N+1):
      if not utils.isPrime(j):
        continue
      ij = int(str(i) + str(j))
      if not utils.isPrime(ij):
        continue
      ji = int(str(j) + str(i))
      if not utils.isPrime(ji):
        continue
      g[i].append(j)
      g[j].append(i)

  for node in g:
    v[len(g[node])].append(node)

  return g, v


def is_in_clique(n, g):
  """Returns whether or not node n is in a clique. 

  Args:
    n: node to check if is in clique or not.
    g: prime pairs graph.

  Returns:
    Set of nodes in the clique that contains n. 
  """

  neighbors = g[n]
  common_nodes = set(neighbors).union((n,))
  for neighbor in neighbors:
    common_nodes = common_nodes.intersection(set(g[neighbor]).union((neighbor,)))
  return common_nodes

if __name__ == '__main__':
  # Tests
  g, v = make_pairs(10)
  assert(7 in g[3])
  assert(3 in g[7])
  assert(v[1] == [3, 7])

  assert(is_in_clique(3, g) == set((3, 7)))

  logger.info('Tests passed. ')

  N = 10**4  # Largest prime in the prime pairs graph. 
  g, v = make_pairs(N)

  lowest_sum = np.inf
  lowest_clique = None

  clique_size = 4
  for num_edges in range(clique_size-1, max(v)):
    for node in v[num_edges]:
      clique = is_in_clique(node, g)
      if clique and len(clique) == clique_size:
        if sum(clique) < lowest_sum:
          lowest_sum = sum(clique)
          lowest_clique = clique

  print(lowest_sum)
  print(lowest_clique)

  """
  logger.info(len(g))
  logger.info(len(v[5]))
  logger.info(len(v[6]))
  logger.info(v[6])
  logger.info(g)
  logger.info(v)
  """

  logger.info('Finished. ')

