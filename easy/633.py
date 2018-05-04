class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        is_square = lambda x: math.sqrt(x) == int(math.sqrt(x)) if x > 0 else True
        for i in range(0, max(2, c // 2 + 1)):
            if i ** 2 > c:
                break
            if is_square(c - i ** 2):
                return True

        return False