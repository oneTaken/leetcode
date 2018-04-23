class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = []
        count = dict()
        index = dict()
        for i, c in enumerate(s):
            if count.get(c) is None:
                keys.append(c)
                count[c] = 1
                index[c] = i
            else:
                count[c] += 1
                index[c] = i

        for key in keys:
            if count[key] == 1:
                return index[key]

        return -1