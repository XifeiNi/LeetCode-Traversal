class TrieNode:
    def __init__(self, letter):
        self.children = {}
        self.isEnd = False
        self.sentence = None
        self.hot = 0
        self.letter = letter


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode('')
        self.searchTerm = ""
        for sentence, time in zip(sentences, times):
            self.addSearch(sentence, time)
            
    
    def addSearch(self, sentence, hot):
        root = self.root
        for c in sentence:
            if c not in root.children:
                root.children[c] = TrieNode(c)
            root = root.children[c]
        root.isEnd = True
        root.sentence = sentence
        root.hot -= hot
    
    def dfs(self, trienode):
        ret = []
        if trienode:
            if trienode.isEnd:
                ret.append((trienode.hot, trienode.sentence))
            for child in trienode.children:
                ret.extend(self.dfs(trienode.children[child]))
        return ret
        
    
    def search(self, keyword):
        root = self.root
        for c in keyword:
            if c not in root.children:
                return []
            root = root.children[c]
        return self.dfs(root)

    def input(self, c: str) -> List[str]:
        result = []
        if c != '#':
            self.searchTerm += c
            result = self.search(self.searchTerm)
        else:
            self.addSearch(self.searchTerm, 1)
            self.searchTerm = ""
        return [item[1] for item in sorted(result)[:3]]
            


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
