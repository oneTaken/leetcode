class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums) // 2
        keys = list(set(nums))
        data = dict().fromkeys(keys, 0)
        for num in nums:
            data[num] += 1
        for key in keys:
            if data[key] > mid:
                return key