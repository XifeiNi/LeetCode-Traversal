from collections import defaultdict
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        pairMap = self.convertMapFromPairs(pairs)
        for w1, w2 in zip(words1, words2):
            found = False
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2:
                    found = True
                    break
                for w in pairMap[word]:
                    if w not in seen:
                        stack.append(w)
                        seen.add(word)
            if not found:
                return False
        return True
        
    
    def convertMapFromPairs(self, pairs):
        pairMap = defaultdict(set)
        for pair in pairs:
            pairMap[pair[0]].add(pair[1])
            pairMap[pair[1]].add(pair[0])
        return pairMap
