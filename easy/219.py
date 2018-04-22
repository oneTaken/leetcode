# solution1
# exceed time
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        for i in range(length):
            start = max(0, i - k)
            end = min(length, i + k)
            region = list(range(start, end))
            for j in region:
                if i != j and nums[i] == nums[j]:
                    return True

        return False

# solution2
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        keys = list(set(nums))
        data = dict().fromkeys(keys, None)

        for i in range(length):
            if data.get(nums[i]) is None:
                data[nums[i]] = [i]
            else:
                data[nums[i]].append(i)

        for key in keys:
            if len(data[key]) > 1:
                for j in range(len(data[key]) - 1):
                    if data[key][j] + k >= data[key][j + 1]:
                        return True

        return False