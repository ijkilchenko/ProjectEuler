from math import floor

cache = {}

def get_parts(n):
  """
  Returns the partitions of n, including n,
  where the partitions are sorted in increasing
  order keyed by the first number in each partition.
  Each partition is sorted in decreasing order.

  E.g. if n = 4:
  [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]
  Observe that successive partition starts with the same 
  or larger number than the previous. 
  Inside each partition, the numbers are sorted in decreasing
  order.
  """

  # Check if we have done this subproblem before
  if n in cache:
    return cache[n]
  
  # Base case (only need one because the recursive function
  # doesn't jump more than one value backwards). 
  if n == 1:
    return [(1,)]
  
  # Recursive step
  # We "subtract" off numbers from n, and each number then
  # "leads" the cached partitions.
  # E.g. if n = 4:
  # We subtract off 1, and get the cached partitions for n=3,
  # we then add only the partitions of n=3 which start with 1 
  # or less. Then we do the same thing with 2 and add only the
  # partitions of n=2 which start with 2 or less. Etc. This
  # strategy guarantees that we are adding unique partitions 
  # to the list (because we first add only partitions that start
  # with a 1, then only the partitions that start with a 2, etc.).
  # This scheme also keeps our list of partitions sorted (as
  # described in the docstring). Because they are sorted, this
  # allows us to use 'break' to skip the partitions that start
  # with a number larger than the one we used for the "subtraction."
  partitions = []
  for i in range(1, n):  # These are the numbers we are "subtracting"
    parts = get_parts(n-i)  # Get partitions in the sorted order.
    for part in parts:
      # Keep adding partitions until this sorting condition is violated
      if part[0] > i:  
        break
      else:
        partitions.append((i,) + part)
  # Append the "root" (turned out to be easier to do it this way)
  partitions.append((n,))  
  cache[n] = partitions
  
  return cache[n]


def get_num_parts(n):
  all_parts = get_parts(n)
  print(all_parts)
  return len(all_parts) - 1

if __name__ == '__main__':
  print(get_num_parts(5))

