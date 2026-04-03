class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.num_map = {}

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        self.lst.append(val)
        self.num_map[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.num_map:
            last = self.lst[-1]
            #change the element we want to delete to the last ele in lst
            self.lst[self.num_map[val]] = last
            #now change idx of last element to reflect idx of deleted one
            self.num_map[last] = self.num_map[val]
            self.lst.pop()
            del self.num_map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()