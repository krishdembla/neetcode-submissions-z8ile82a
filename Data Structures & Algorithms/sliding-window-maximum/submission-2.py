class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Input: nums = [1,2,1,0,4,2,6], k = 3
        #Output: [2,2,4,4,6]
        l, r = 0, 0
        q = deque()
        result = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if(r+1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        
        return result
