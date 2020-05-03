class SnapshotArray:

    def __init__(self, length):
        self.dic = defaultdict(dict)
        self.snap_id = 0
        
        
    def set(self, index, val):
        self.dic[self.snap_id][index] = val
        

    def snap(self):
        self.snap_id += 1
        self.dic[self.snap_id] = self.dic[self.snap_id - 1].copy()
        return self.snap_id -1
        

    def get(self, index, snap_id):
        if index in self.dic[snap_id]:
            return self.dic[snap_id][index]
        else:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
