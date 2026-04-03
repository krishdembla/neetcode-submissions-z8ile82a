class TimeMap:

    def __init__(self):
        self.item_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.item_map:
            self.item_map[key].append([timestamp, value])
        else:
            self.item_map[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.item_map[key]) - 1
        res = ""
        arr = self.item_map.get(key, [])
        if not arr:
            return ""
        
        while l <= r:
            mid = l + (r-l) // 2
            if timestamp < arr[mid][0]:
                r = mid - 1 #look inside left half since the mid element was created after the given timestamp 
            else:
                res = arr[mid][1] #set most recent timestamp here
                l = mid + 1 #try to find a later valid timestamp
        return res



