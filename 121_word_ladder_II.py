from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}
        
        self.bfs(end, start, distance, dict)
        results = []
        self.dfs(start, end, distance, dict, [start],  results)
        return results


    def bfs(self, start, end, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for word in self.getNextWords(node, dict):
                if word not in distance:
                    distance[word] = distance[node] + 1
                    queue.append(word)
        
    
    def getNextWords(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words

    def dfs(self, current, target, distance, dict, path, results):
        if current == target:
            results.append(list(path))
            return
        
        for word in self.getNextWords(current, dict):
            if distance[word] != distance[current] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()
            
