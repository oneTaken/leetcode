class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_one = 0
        start = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if start is None:
                    start = i
            else:
                if start is None:
                    continue
                max_one = max(max_one, i - start)
                start = None

        if start is not None:
            max_one = max(max_one, i + 1 - start)

        return max_one