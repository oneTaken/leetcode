class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        index = list(range(ord('a'), ord('z') + 1)) + list(range(ord('0'), ord('9') + 1))
        data = ''.join([c for c in s.lower() if ord(c) in index])

        return data == data[::-1]