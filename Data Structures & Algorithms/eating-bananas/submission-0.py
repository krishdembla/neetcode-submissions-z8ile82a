class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #sort the array + perform binary search
        #at the middle element in the binary search, set that middle element as the rate
        #if the hours taken for that rate < h then we can move to left half of bin search
        low = 1
        high = max(piles)
        minn = high

        def numHours(rate, piles):
            count = 0
            for i in piles:
                count += (i + rate -1) // rate
            return count


        while low <= high:
            mid = low + (high - low) // 2
            hrs = numHours(mid, piles)
            if hrs <= h:
                high = mid - 1
                minn = mid
            else:
                low = mid + 1
        return minn
            
            

           

