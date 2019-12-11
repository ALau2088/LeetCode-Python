# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        def recursion(root, L, R):
            nonlocal sum
            if root.val >= L and root.val <= R:
                sum+=root.val
            if root.left:
                recursion(root.left, L, R)
            if root.right:
                recursion(root.right, L, R)
            return
        recursion(root, L, R)
        return sum

# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# root = {val: 10, left: {val: 5, left:{val: 3, left: None, right: None}, right:{val: 7, left: None, right: None}, right: {val: 15 left:{null}, right:{val: 18, left: None, right: None}}}
# Output: 32

# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23