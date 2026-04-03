class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        res = 0

        while l<r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            #only checking for smaller column because we can iterate further and find a next column (shorter than r) which is taller and gives more area
            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
            
        return res
            
