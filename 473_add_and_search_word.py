class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        
    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        if word is None:
            return False
        return self.search_(self.root, word, 0)
    def search_(self, node, word, index):
        if node is None:
            return False
        
        if index >= len(word):
            return node.is_word
        
        if word[index] != '.':
            return self.search_(node.children.get(word[index]), word, index + 1)
        for child in node.children:
            if self.search_(node.children[child], word, index + 1):
                return True
        return False
