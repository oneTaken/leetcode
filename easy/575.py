class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        length = len(candies)
        kinds = len(set(candies))

        return length // 2 if kinds >= length // 2 else kinds
