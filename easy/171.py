class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        times = 1
        count = 0
        start = ord('A')
        for c in s[::-1]:
            num = ord(c) - start + 1
            count += num * times
            times *= 26

        return count