
class Solution:
    def _getNumToFreq(self, secret, guess):
        numToFrequency = collections.defaultdict(int)
        bulls = 0
        for index, char in enumerate(secret):
            if char == guess[index]:
                bulls += 1
            else:
                numToFrequency[char] += 1
        return (bulls, numToFrequency)
    def getHint(self, secret: str, guess: str) -> str:
        bulls, numToFrequency = self._getNumToFreq(secret, guess)
        cows = 0
        for index, char in enumerate(guess):
            if char == secret[index]:
                continue
            if numToFrequency[char] == 0:
                continue
            else:
                cows += 1
            numToFrequency[char] -= 1
        return str(bulls) + "A" + str(cows) + "B"
    
            