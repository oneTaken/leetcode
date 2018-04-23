# solution1
# exceed time 732/741
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

# solution2
# exceed time 734/741
class Solution2:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = bool(sum(nums) % 2)
        for i in range(len(nums)):
            if bool(nums[i] % 2) ^ flag:
                continue
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

# solution3
# exceed time 740/741
class Solution3:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        flag = bool(total % 2)
        for i in range(len(nums)):
            if bool(nums[i] % 2) ^ flag:
                continue
            if sum(nums[:i]) * 2 == total - nums[i]:
                return i
        return -1

# solution4
class Solution4:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i

            left += nums[i]

        return -1