class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [0 for _ in range(length)]
        for i in range(length):
            ans[nums[i] - 1] += 1

        return [i + 1 for i in range(length) if ans[i] == 0]