class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        length = len(nums2)
        flag = True
        for num in nums1:
            index = nums2.index(num)
            flag = True
            for j in range(index + 1, length):
                if nums2[j] > num:
                    ans.append(nums2[j])
                    flag = False
                    break
            if flag:
                ans.append(-1)

        return ans
