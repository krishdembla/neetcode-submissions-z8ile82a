class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hm = {}
         for num in nums:
            if num not in hm.keys():
                hm[num] = 1
            else:
                hm[num] += 1
                return True
        
         return False