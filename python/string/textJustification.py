class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results, line, length = [], [], 0
        for word in words:
            if len(word)  + len(line) + length <= maxWidth:
                length += len(word)
                line.append(word)
            else:
                results.append(self.formatLine(line, maxWidth))
                length = len(word)
                line = [word]
        if len(line) > 0:
            results.append(self.formatLastLine(line, maxWidth))
        return results
    def formatLine(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        s, gaps = line[0], len(line) - 1
        for index, w in enumerate(line[1:]):
            if index < (maxWidth - length) % gaps:
                s = s + " " + " " * ((maxWidth - length) // gaps) + w
            else:
                s = s + " " * ((maxWidth - length) // gaps) + w
        return s
    def formatLastLine(self, line, maxWidth):
        s = ' '.join(line)
        return s + " " * (maxWidth - len(s))
