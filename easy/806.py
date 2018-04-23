class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        start = ord('a')
        count = 1
        num = 0
        for c in S:
            width = widths[ord(c) - start]
            if num + width > 100:
                count += 1
                num = width
            else:
                num += width

        return count, num