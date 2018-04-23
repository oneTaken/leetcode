class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = list(s)
        index = []
        chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i] in chars:
                index.append(i)
        flip_index = index[::-1]
        for i in range(len(index)):
            new_s[index[i]] = s[flip_index[i]]

        return ''.join(new_s)