class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        n_length = len(needle)
        for i in range(len(haystack) - n_length + 1):
            if haystack[i:i + n_length] == needle:
                return i

        return -1