class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        keys = list(set(s))
        data = dict().fromkeys(keys, 0)
        for c in s:
            data[c] += 1

        for c in t:
            if data.get(c) is None or data[c] <= 0:
                return False
            else:
                data[c] -= 1

        return True
