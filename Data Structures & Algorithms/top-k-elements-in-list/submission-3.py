import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        buckets= [[] for _ in range(len(nums) + 1)]

        for num,freq in freq_map.items():
            buckets[freq].append(num) #we set freq as key because then the last bucket holds the most freq
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
        return []


