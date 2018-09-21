from math import floor

cache = {}

def get_parts(n):
  # Returns the partitions of n
  if n in cache:
    return cache[n]
  
  if n == 1:
    return [(1,)]
  if n == 2:
    return [(1, 1)]
  
  # Recursive step
  partitions = set()
  for i in range(1, n):
    if n-i >= i:
      partitions.add((n-i, i))
    for part in get_parts(n-i):
      if part[0] > i:
        break
      else:
        partitions.add((i,) + part)
  partitions = list(partitions)
  partitions.sort(key=lambda x: x[0])
  cache[n] = partitions
  
  return cache[n]


def get_num_parts(n):
  all_parts = get_parts(n)
  return len(all_parts)

if __name__ == '__main__':
  print(get_num_parts(100))

