class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = bin(n)[2:]
        start = '10'
        if len(num) % 2 == 1:
            start = '01'
            num = '0' + num

        return start * (len(num) // 2) == num