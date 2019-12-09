class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        number = str(n)
        product = 1;
        sum = 0;
        for digit in number:
            product = product * int(digit)
            sum = sum + int(digit)
        return product - sum