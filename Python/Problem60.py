import utilsPrimes as utils
import logging
import numpy as np
import itertools
from functools import reduce
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def make_pairs(N):
  """Makes a prime pairs graph.
  
  Args:
    N: Largest possible prime in the prime pairs graph.

  Returns:
    A dictionary. 
  """

  g = defaultdict(lambda: [])

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

  return g


def is_clique(c, g):
  """Returns whether or not nodes in c form a clique.  

  Args:
    c: list of nodes. 
    g: prime pairs graph.

  Returns:
    A boolean indicating whether or not nodes in c form a clique. 
  """

  common_nodes = set([node for node in c])

  for node in c:
    common_nodes = common_nodes.intersection(set(g[node]).union((node,)))

  if common_nodes == set(c):
    return True
  else:
    return False


def get_next_combs(N, n=4):
  """Inspired by: https://math.stackexchange.com/a/89453/100900
  """

  A = [0]*len(N)
  L = [set()]
  S = [0]
  j = 1
  while any(elem is not None for elem in A):
    i_star = np.argmin([S[A[i]] + N[i] if A[i] is not None else np.inf for i in range(0, len(N))])
    comb = L[A[i_star]].union((N[i_star],))
    L.append(comb)
    if len(comb) == n:
      yield comb
    S.append(S[A[i_star]] + N[i_star])
    i = A[i_star]
    A[i_star] = None
    for i_next in range(i+1, len(L)):
      if N[i_star] > max(L[i_next]):
        A[i_star] = i_next
        break


def grow_clique(c, g):
  """Takes a clique c and checks all its neighbors to see if the clique can be 
  grown and returns all valid bigger cliques that contain c.
  """

  neighbors = reduce(lambda x, y: x.union(y), [g[node] for node in c], set())

  cliques = []
  for neighbor in neighbors:
    new_clique = list(c) + [neighbor]
    if neighbor not in c and is_clique(new_clique, g):
      cliques.append(new_clique)
 
  return cliques

if __name__ == '__main__':
  # Tests
  g = make_pairs(20)
  assert(7 in g[3])
  assert(3 in g[7])

  assert(is_clique([3, 7], g) == True)

  # print(grow_clique([1, 2], {1:[2,3], 2:[1,3], 3:[1,2]}))

  for comb in get_next_combs(list(g.keys()), 3):
    # print(sum(comb), comb)
    pass

  logger.info('Tests passed. ')

  N = 9000  # Largest prime in the prime pairs graph. 
  g = make_pairs(N)

  cliques = [c for c in itertools.combinations(g, 3) if is_clique(c, g)]

  for _ in range(1, 3):
    new_cliques = []
    for clique in cliques:
      new_cliques.extend(grow_clique(clique, g))
    cliques = new_cliques

  lowest_sum = np.inf
  lowest_clique = None

  for clique in cliques:
    if sum(clique) < lowest_sum:
      lowest_sum = sum(clique)
      lowest_clique = clique

  logger.info(lowest_sum)
  logger.info(lowest_clique)

  logger.info('Finished. ')

