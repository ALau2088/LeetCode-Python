class Solution:
    # grid: , int: are optional function annotations per python3.6.
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # print(type(grid)) # <class 'list'>
        row_maxes = [max(row) for row in grid]  # [8, 7, 9, 3]
        # [9, 4, 8, 7] # The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))  # sum([res1,res2,...]); see List Comprehensions

# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]

# The grid after increasing the height of buildings without affecting skylines is:

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]


Obj = Solution()
print(Obj.maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
