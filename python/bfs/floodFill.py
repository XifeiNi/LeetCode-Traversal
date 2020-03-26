from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = deque([(sr, sc)])
        old = image[sr][sc]
        image[sr][sc] = newColor
        if newColor == old:
            return image
        while queue:
            x, y = queue.popleft()
            for deltaX, deltaY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + deltaX < len(image) and 0 <= y + deltaY < len(image[0]) and image[x + deltaX][y + deltaY] == old:
                    queue.append((x + deltaX, y + deltaY))
                    image[x + deltaX][y + deltaY] = newColor
        
        return image
