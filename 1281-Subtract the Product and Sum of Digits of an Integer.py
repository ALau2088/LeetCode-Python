class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        number = str(n)
        product = 1
        sum = 0
        for digit in number:
            product = product * int(digit)
            sum = sum + int(digit)
        return product - sum

# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15


Obj = Solution()
print(Obj.subtractProductAndSum(234))
