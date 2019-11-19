from collections import defaultdict
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dictionary = defaultdict(list)
        i = 0
        for word in words:
            self.dictionary[word].append(i)
            i+=1
        
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1List = self.dictionary[word1]
        word2List = self.dictionary[word2]
        i, j = 0, 0
        minimum = sys.maxint
        while i < len(word1List) and j < len(word2List):
            index1 = word1List[i]
            index2 = word2List[j]
            if index1 < index2:
                minimum = min(minimum, index2 - index1)
                i+=1
            else:
                minimum = min(minimum, index1 - index2)
                j+=1
        return minimum
                
