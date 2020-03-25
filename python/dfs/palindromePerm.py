class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = collections.defaultdict(int)
        for char in s:
            count[char] += 1
        odd_c = ""
        odds = 0
        ret = []
        for char, freq in count.items():
            if freq %2 == 1:
                odd_c = char
                odds += 1
            if odds > 1:
                return []
        half = []
        for char, freq in count.items():
            half.extend([char] * (freq//2))
        visited = [False] * len(half)
        self.dfs(half, visited, [], ret)
        results = []
        for permutation in ret:
            first = ''.join(permutation)
            last = ''.join(reversed(permutation))
            if odds == 1:
                results.append(first + odd_c + last)
            else:
                results.append(first + last)
        return results
    def dfs(self, half, visited, perm, ret):
        if len(perm) == len(half):
            ret.append(perm[:])
            return
        for i in range(len(half)):
            if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                continue
            visited[i] = True
            perm.append(half[i])
            self.dfs(half, visited, perm, ret)
            perm.pop()
            visited[i] = False
