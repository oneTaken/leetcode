class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0 and s[:i] * (length // i) == s:
                return True

        return False