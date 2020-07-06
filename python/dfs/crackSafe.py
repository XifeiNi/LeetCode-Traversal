class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total = math.pow(k, n)
        starting_str = "0" * (n - 1)
        visited = set()
        path = []
        self.dfs(starting_str, k, total, path, visited)
        return starting_str + "".join(path)
    
    def dfs(self, starting_str,  k, total, path, visited):
        if total == len(visited):
            return True
        
        for i in range(k):
            next_str = starting_str + str(i)
            if next_str not in visited:
                
                path.append(str(i))
                visited.add(next_str)
                if not self.dfs(next_str[1:], k, total, path, visited):
                    visited.remove(next_str)
                    path.pop()
                else:
                    return True
        return False
