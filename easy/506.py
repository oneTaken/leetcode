class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort_score = sorted(nums)
        length = len(nums)
        ans = [0 for _ in range(length)]

        if length >= 1:
            gold_index = nums.index(sort_score[length - 1])
            ans[gold_index] = 'Gold Medal'

        if length >= 2:
            silver_index = nums.index(sort_score[length - 2])
            ans[silver_index] = 'Silver Medal'

        if length >= 3:
            bronze_index = nums.index(sort_score[length - 3])
            ans[bronze_index] = 'Bronze Medal'

        for i in range(length - 4, -1, -1):
            index = nums.index(sort_score[i])
            ans[index] = str(length - i)

        return ans