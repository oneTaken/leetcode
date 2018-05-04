class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        max_width = int(math.floor(math.sqrt(area)))
        for w in range(max_width, 0, -1):
            if area / w == area // w:
                return [area // w, w]
