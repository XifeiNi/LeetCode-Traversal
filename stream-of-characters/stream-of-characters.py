class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
    def search(self, word):
        node = self.find(word)
        return node is not None and node.isWord
    def startsWith(self, prefix):
        return self.find(prefix) is not None
class StreamChecker:
    def __init__(self, words: List[str]):
        self.keyValue = Trie()
        self.currentKeyCodes = []
        for word in words:
            self.keyValue.insert(reversed(word))

    def query(self, letter: str) -> bool:
        self.currentKeyCodes.append(letter)
        start, end = len(self.currentKeyCodes), len(self.currentKeyCodes)
        while start >= 0:
            if not self.keyValue.startsWith(''.join(reversed(self.currentKeyCodes[start:end]))):
                return False
            if self.keyValue.search(''.join(reversed(self.currentKeyCodes[start:end]))):
                return self.keyValue.find(''.join(reversed(self.currentKeyCodes[start:end]))).isWord
            start -= 1
        return False



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)