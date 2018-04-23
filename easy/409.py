class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = list(set(s))
        count = dict().fromkeys(keys, 0)
        for c in s:
            count[c] += 1

        ans = [count[key] // 2 * 2 for key in keys]
        ans = sum(ans)

        plus = bool(sum([1 for key in keys if count[key] % 2 == 1]))

        return ans + plus