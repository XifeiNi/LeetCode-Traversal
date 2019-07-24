import random

class RandomizedSet:
    
    def __init__(self):
        self.nums = []
        self.pos = {}
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.pos:
            return False
        idx, last = self.pos[val], self.nums[-1]
        self.nums[idx], self.pos[last] = last, idx
        self.nums.pop()
        del self.pos[val]
        return True
    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
