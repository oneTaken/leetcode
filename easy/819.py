class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()

        for sign in ['!', '?', ',', ';', '.', '\'']:
            paragraph = paragraph.replace(sign, ' ')

        print(paragraph)
        blank = []
        start = None

        for i, c in enumerate(paragraph):
            if c == ' ':
                if start is None:
                    start = i
            else:
                if start is not None and i - start > 1:
                    blank.append((start, i))
                start = None
        if start is not None:
            blank.append((start, len(paragraph)))

        paragraph = list(paragraph)
        for (start, end) in blank:
            paragraph[start:end] = ' ' + ',' * (end - start - 1)

        paragraph = ''.join(paragraph).replace(',', '')
        words = []
        for word in paragraph.split():
            if word not in banned:
                words.append(word)

        count = dict().fromkeys(list(set(words)), 0)
        for word in words:
            count[word] += 1

        num_word = [(v, k) for k, v in count.items()]
        num_value = lambda x: x[0]
        sorted_num_word = sorted(num_word, key=num_value, reverse=True)

        return sorted_num_word[0][1]
