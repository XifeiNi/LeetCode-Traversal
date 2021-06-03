class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentLine, length, results = [], 0, []
        for word in words:
            if length  + len(word) + len(currentLine) <= maxWidth:
                length += len(word)
                currentLine.append(word)
            else:
                results.append(self.format(currentLine, maxWidth))
                length = len(word)
                currentLine = [word]
        if len(currentLine):
            results.append(self.formatLast(currentLine, maxWidth))
        return results
    def format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        result, gaps = line[0], len(line) - 1
        for index, word in enumerate(line[1:]):
            if index < (maxWidth - length) % gaps:
                result = result + " " + " " * ((maxWidth - length) // gaps) + word
            else:
                result = result + " " * ((maxWidth - length) // gaps) + word
        return result
    def formatLast(self, line, maxWidth):
        result = ' '.join(line)
        return result + " " * (maxWidth - len(result))
    