# solution1
# 空间复杂度不是常数复杂度，为O(n)
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [x for x in nums if x > 0]
        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 1
        for i in range(1, nums[-1] + 1):
            if i < nums[i - 1]:
                return i

        return len(nums) + 1