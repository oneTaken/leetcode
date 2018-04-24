class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if (target - num) in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(target-num)]