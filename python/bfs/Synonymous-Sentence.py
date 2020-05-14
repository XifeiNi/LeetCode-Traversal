from collections import deque, defaultdict

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        queue = deque([text])
        graph = self.buildGraph(synonyms)
        ans = set()
        
        while queue:
            curr = queue.popleft()
            ans.add(curr)
            wordList = curr.split()
            for i, word in enumerate(wordList):
                for synonym in graph[word]:
                    newSentence = ' '.join(wordList[:i] + [synonym] + wordList[i + 1:])
                    if newSentence not in ans:
                        queue.append(newSentence)
        return sorted(list(ans))
                    
        
    def buildGraph(self, synonyms):
        graph = defaultdict(set)
        
        for wordA, wordB in synonyms:
            graph[wordA].add(wordB)
            graph[wordB].add(wordA)
        return graph
