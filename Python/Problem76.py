class SumData:
  def __init__(self, n):
    self.n = n
    self.eyes = {1: 1}  # i to # of partitions of n-1

  def fill_eyes(self, older_data):
    for i in range(2, n):
      i_or_less = min(i, max(older_data[n-i].eyes.keys()))
      self.eyes[i] = older_data[n-i].eyes[i_or_less] + self.eyes[i-1]
    self.eyes[n] = self.eyes[n-1] + 1

if __name__ == '__main__':
  data = {1: SumData(1)}
  N = 100

  for n in range(2, N+1):
    sum_data = SumData(n)
    sum_data.fill_eyes(data)
    data[n] = sum_data

  print(data[N].n, data[N].eyes[N] - 1)

