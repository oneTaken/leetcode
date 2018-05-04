# solution1
# exceed time 36/40
class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n + 1):
            count += str(i).count('1')

        return count