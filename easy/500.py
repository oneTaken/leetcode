class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        data = dict().fromkeys(s[0], 0)
        data.update(dict().fromkeys(s[1], 1))
        data.update(dict().fromkeys(s[2], 2))

        output = []
        for word in words:
            index = [data[c] for c in word.lower()]
            if index == [index[0]] * len(index):
                output.append(word)

        return output