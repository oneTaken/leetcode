class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numbers = set(nums1) & set(nums2)
        ans = []
        for num in numbers:
            sub_ans = [num] * (min(nums1.count(num), nums2.count(num)))
            ans.extend(sub_ans)

        return ans