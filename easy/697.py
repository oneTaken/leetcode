class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        keys = list(set(nums))
        count = dict().fromkeys(keys, None)
        for i, num in enumerate(nums):
            if count[num] is None:
                count[num] = [i]
            else:
                count[num].append(i)
        degrees = [len(count[keys[i]]) for i in range(len(keys))]
        degree = max(degrees)

        index = []
        min_length = len(nums)
        for i in range(len(keys)):
            if len(count[keys[i]]) == degree:
                length = count[keys[i]][-1] - count[keys[i]][0] + 1
                min_length = min(min_length, length)

        return min_length