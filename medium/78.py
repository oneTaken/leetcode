class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        ans = []
        for i in range(len(nums) + 1):
            _ans = itertools.combinations(nums, i)
            _ans = list(map(list, _ans))
            ans.extend(_ans)

        return ans