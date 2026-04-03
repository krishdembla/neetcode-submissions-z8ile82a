
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #building the freq map by iterating thru list and adding
        freq_map={}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        #using a min heap to store k most frequent elements
        mh = []
        for key,value in freq_map.items():
            heapq.heappush(mh,(value,key)) #adding freq,key in tuple form to list minheap mh
            #add first, then check if len > k
            if len(mh) > k:
                heapq.heappop(mh) #removing the first most min element

        #getting results from heap
        res = []
        while mh:
            res.append(heapq.heappop(mh)[1]) #getting whatever keys left in the minheap
        
        res.reverse() #since we were using minheap we reverse to get most frequent elements first
        return res
            
