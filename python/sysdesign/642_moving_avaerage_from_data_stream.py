from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.queue = deque([])
        self.size = size
        self.sum = 0.0
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        if len(self.queue) >= self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum+=val
        return self.sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
