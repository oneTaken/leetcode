# solution1
# exceed time 6/84
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        while len(set(nums)) != 1:
            index = nums.index(max(nums))
            nums = [x + 1 for x in nums]
            nums[index] -= 1
            count += 1

        return count