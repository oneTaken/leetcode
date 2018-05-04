# 使用problem 451的部分函数
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        keys = list(set(nums))
        count = dict().fromkeys(keys, 0)
        for num in nums:
            count[num] += 1

        func = lambda x: x[1]
        k_v = [(k, v) for k, v in count.items()]
        sort_kv = sorted(k_v, key=func, reverse=True)
        ans = [k for k, v in sort_kv][:k]

        return ans
