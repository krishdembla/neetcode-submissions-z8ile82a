class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #nums contains n int (len)
        ans = 0
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                ans = int(i)
                break
        return ans