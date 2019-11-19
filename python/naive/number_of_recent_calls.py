class RecentCounter:

    def __init__(self):
        self.pings = []
        self.size = 0

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.size+=1
        while self.size and self.pings[0] < t - 3000:
            del self.pings[0]
            self.size-=1
        return self.size
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
