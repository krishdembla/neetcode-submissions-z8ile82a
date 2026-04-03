class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        result = 0

        l = 0 #left pointer
        max_freq = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            max_freq = max(max_freq, counter[s[r]])

            while ((r-l+1) - max_freq) > k:
                counter[s[l]] -= 1 #decrease freq of char at left pointer
                l += 1 #shrink the window
            result = max(result, r - l + 1)
        
        return result