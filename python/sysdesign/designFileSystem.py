class FileSystem:

    def __init__(self):
        self.val = {}

    def createPath(self, path: str, value: int) -> bool:
        words = path.split('/')[1:-1]
        s = ""
        for word in words:
            s += "/" + word
            if s not in self.val:
                return False
        if path in self.val and self.val[path] != value:
            return False
        self.val[path] = value
        return True
            

    def get(self, path: str) -> int:
        if path not in self.val:
            return -1
        return self.val[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
