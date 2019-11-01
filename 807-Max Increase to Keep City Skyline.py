class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int: # grid: , int: are optional function annotations per python3.6.
    # print(type(grid)) # <class 'list'>
    row_maxes = [max(row) for row in grid] # [8, 7, 9, 3]
    col_maxes = [max(col) for col in zip(*grid)] # [9, 4, 8, 7]

    return sum(min(row_maxes[r], col_maxes[c]) - val
      for r, row in enumerate(grid)
      for c, val in enumerate(row))