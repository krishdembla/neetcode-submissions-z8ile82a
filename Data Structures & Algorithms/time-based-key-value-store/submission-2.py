class TimeMap:

    def __init__(self):
        self.item_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.item_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.item_map:
            return ""
        
        if timestamp < self.item_map[key][0][0]:
            return ""
        
        l = 0
        r = len(self.item_map[key]) - 1
        
        
        while l <= r:
            mid = l + (r-l) // 2
            if timestamp == self.item_map[key][mid][0]:
                return self.item_map[key][mid][1] 
            elif timestamp < self.item_map[key][mid][0]:
                r = mid - 1 #since mid timestamp is greater, we know we can look left for a more recent timestamp
            else:
                l = mid + 1
        return self.item_map[key][r][1]



