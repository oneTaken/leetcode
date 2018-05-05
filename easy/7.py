class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        ans = int(str(abs(x))[::-1]) * sign

        return ans if ans >= -1 * 2 ** (31) and ans <= 2 ** (31) else 0
