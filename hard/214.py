class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        for i in range(len(s)//2, -1, -1):
            # mid
            if s[:i][::-1] == s[i+1:2*i+1]:
                return s[i+1:][::-1] + s[i] + s[i+1:]
            # left
            if s[:i+1][::-1] == s[i+1:2*i+2]:
                return s[i+1:][::-1] + s[i+1:]
            # right
            if s[:i][::-1] == s[i:2*i]:
                return s[i:][::-1] + s[i:]