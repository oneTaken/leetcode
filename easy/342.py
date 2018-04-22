class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and bin(num).count('1')== 1 and bin(num)[2:].count('0') % 2 == 0