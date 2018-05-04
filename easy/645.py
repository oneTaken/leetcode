class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        nums = sorted(nums)
        replace = None
        miss = None
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > i:
                miss = i
                replace = sum(nums) + miss - (length * (length + 1)) // 2
                break
            elif nums[i - 1] < i:
                replace = nums[i - 1]
                miss = (length * (length + 1)) // 2 - sum(nums) + replace
                break

        return replace, miss
