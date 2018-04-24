class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum_str = lambda x: sum(list(map(int, x)))
        while len(str(num)) > 1:
            num = sum_str(str(num))

        return num