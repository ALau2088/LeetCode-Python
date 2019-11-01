class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int: # grid: , int: are optional function annotations per python3.6.
    print(type(grid)) # <class 'list'>
    row_maxes = [max(row) for row in grid]
    col_maxes = [max(col) for col in zip(*grid)]