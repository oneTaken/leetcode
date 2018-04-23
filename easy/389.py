class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        keys = list(set(s))
        keys2 = list(set(t))
        if len(keys) < len(keys2):
            return list(set(keys2) - set(keys))[0]

        data = dict().fromkeys(keys, 0)
        for char in s:
            data[char] += 1
        for char in t:
            data[char] -= 1

        value = [key for key in keys if data[key] == -1]

        return value[0]