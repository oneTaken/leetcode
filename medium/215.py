class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_list = sorted(nums, reverse=True)

        return num_list[k - 1] if len(num_list) >= k else num_list[-1]