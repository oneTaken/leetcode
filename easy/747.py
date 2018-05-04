class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        sort_num = sorted(nums)
        max_num = sort_num[-1]
        sec_num = sort_num[-2]

        ans = nums.index(max_num) if max_num >= sec_num * 2 else -1

        return ans