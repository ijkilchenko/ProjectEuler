from math import floor

class V2:
  """
  Proposal:
  We do not need to work with partitions explicitly. Instead we can keep track
  of how many of the partitions start with n or less (still using the sorting
  scheme from V1). If we can reformulate the problem to work without explicit
  partitions, we will essentially be skipping the inner for-loop in the
  recursive step of V1.

  E.g.

  Let's say we have the following data-structure for each n:

  n | i, # of partitions of n-i, sorted with our scheme, that start with i or less

  1 | 1, 1

  2 | 1, 1
    | 2, 2

  3 | 1, 1
    | 2, 2
    | 3, 3

  4 | 1, 1
    | 2, 3
    | 3, 4
    | 4, 5 <- last entry is the "answer" for this n

  Explicit partitions (to make reading easier):
  n=1 > [(1,)]
  n=2 > [(1, 1), (2,)]
  n=3 > [(1, 1, 1), (2, 1), (3,)]
  n=4 > [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]

  Now we use the data-structures for each n to derive the data-structure for n=5

  5 | 1, how many partitions of n=4 start with 1 or less? 1
    | 2, how many partitions of n=3 start with 2 or less? 2
    | 3, '' n=2 '' with 3 or less? 2
    | 4, '' n=1 '' with 4 or less? 1

  1+2+2+1=6
  plus the "root" +1
  7 <- this is the correct answer for the number of partitions of n=5 including
  root.

  So now we can complete the data-structure for n=5

  5 | 1, 1
    | 2, 3=2+1 <- 2 comes from the # of partitions of n=3 with 2 or less. 1 comes from the above entry
    | 3, 5=2+3 <- 2 comes from the # of partitions of n=2 with 3 or less. 3 comes from the above entry
    | 4, 6=1+5 <- 1 comes from the # of partitions of n=1 with 4 or less. 5 comes from the above entry
    | 5, 7
  """

if __name__ == '__main__':
  print(V2.get_num_parts(5))

