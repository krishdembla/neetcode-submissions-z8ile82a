class MyHashMap:

    #basic structure of this is to compute hash, find a bucket and then search for element in that bucket
    #need one extra function -> hash()

    def __init__(self):
        self.length = 1000
        self.lst = [[] for _ in range(self.length)]
    
    def hashing(self, key) -> int:
        return key % self.length

    def put(self, key: int, value: int) -> None:
        idx = self.hashing(key)
        for i, (k,v) in enumerate(self.lst[idx]):
            if k == key: #ensuring 
                self.lst[idx][i] = (key,value)
                return
        self.lst[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self.hashing(key)
        for k,v in self.lst[idx]:
            if k == key:
                return v
        return -1
       
    def remove(self, key: int) -> None:
        idx = self.hashing(key)
        for i, (k,v) in enumerate(self.lst[idx]):
            if k == key:
                self.lst[idx].pop(i)
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)