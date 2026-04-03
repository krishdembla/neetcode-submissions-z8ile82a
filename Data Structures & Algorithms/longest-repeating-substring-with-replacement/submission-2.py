class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #idea is to find a window where the window length - highest freq  <= k (no of replacements allowed)
        #use a sliding window approach and keep expanding window while the constraint holds true
        hm = defaultdict(int)
        l = 0
        best = 0
        max_freq = 0
        for r in range(len(s)):
            hm[s[r]] += 1 #add to hm freq
            max_freq = max(max_freq, hm[s[r]]) #

            while r-l+1 - max_freq > k:
                hm[s[l]] -= 1
                l += 1
            
            best = max(best, r-l+1)
        return best
        

            