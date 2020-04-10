class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queryFreq = [0 for _ in range(len(queries))]
        wordFreq = [0 for _ in range(len(words))]
        ret = []
        for i in range(len(queries)):
            smallest_char = min(queries[i])
            c = collections.Counter(queries[i])
            queryFreq[i] = c[smallest_char]
        
        for i in range(len(words)):
            smallest_char = min(words[i])
            c = collections.Counter(words[i])
            wordFreq[i] = c[smallest_char]

        for i in range(len(queries)):
            count = 0
            for j in range(len(words)):
                if queryFreq[i] < wordFreq[j]:
                    count += 1
            ret.append(count)
        return ret
