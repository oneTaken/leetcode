class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n > 1:
            if n / 3 == n // 3:
                n = n // 3
            else:
                return False

        return True