class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        data = []
        flip = lambda s: s[::-1] if len(s) <= k else s[:k][::-1] + s[k:]
        for c in range(0, len(s), 2 * k):
            data.append(flip(s[c:c + 2 * k]))

        return ''.join(data)