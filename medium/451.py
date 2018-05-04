class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        keys = list(set(s))
        count = dict().fromkeys(keys, 0)
        for c in s:
            count[c] += 1
        func = lambda x: x[1]
        k_v = [(k, v) for k, v in count.items()]
        sort_kv = sorted(k_v, key=func, reverse=True)
        result = [[k * v] for k, v in sort_kv]
        ans = []
        for sub_result in result:
            ans.extend(sub_result)

        return ''.join(ans)
