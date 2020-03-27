class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        blockOpen, lineOpen, ret, bufferLine = False, False, [], ''
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]

                if char == '/' and i + 1 < len(line) and line[i + 1] == '/':
                    while i < len(line):
                        if line[i] == '*' and i + 1 < len(line) and line[i + 1] == '/' and blockOpen:
                            blockOpen = False
                            i += 1
                            break
                        i+=1
                    
                    
                elif char == '/' and i + 1 < len(line) and line[i + 1] == '*' and not blockOpen:
                    blockOpen = True
                    i += 1
                elif char == '*' and i + 1 < len(line) and line[i + 1] == '/' and blockOpen:
                    blockOpen = False
                    i += 1
                elif not blockOpen:
                    bufferLine += char
                i += 1
            if len(bufferLine) > 0 and not blockOpen:
                ret.append(bufferLine)
                bufferLine = ''
        return ret
                    
