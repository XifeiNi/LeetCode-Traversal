class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max = 0
        self.dfs(arr, 0, "")
        return self.max
    def noDup(self, string):
        return len(set(string)) == len(string)
    
    def dfs(self, array, index, s):
        self.max = max(len(s), self.max)
        if index == len(array):
            return
        for i in range(index, len(array)):
            if self.noDup(s + array[i]):
                self.dfs(array, i, s + array[i])
            
        
        
