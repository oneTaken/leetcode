# solution1
# 空间复杂度不是O(1), 是O(n)
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        keys = [1 for _ in range(len(nums))]
        for x in nums:
            keys[x] -= 1
            if keys[x] < 0:
                return x