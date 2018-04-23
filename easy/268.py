class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = set(range(len(nums) + 1)) - set(nums)
        return ans.pop()