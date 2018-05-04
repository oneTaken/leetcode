class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)), reverse=True)

        return nums[2] if len(nums) > 2 else nums[0]
