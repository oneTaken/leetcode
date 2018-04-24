class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.lower() == word or word.upper() == word or (word[0].upper() == word[0] and word[1:].lower() == word[1:])