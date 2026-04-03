class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        #create a hash map of freq of chars in t
        t_freq = {}
        for c in t:
            if c not in t_freq:
                t_freq[c] = 1
            else:
                t_freq[c] += 1
        
        window_freq = {}
        req = len(t_freq)
        formed = 0
        l = 0
        best = float("inf")
        best_l = 0
        for r in range(len(s)):
            #adding r to the window
            if s[r] not in window_freq:
                window_freq[s[r]] = 1
            else:
                window_freq[s[r]] += 1
            
            #if the freq of current char in window is the same as the freq of that same char in t_freq
            if s[r] in t_freq.keys() and window_freq[s[r]] == t_freq[s[r]]:
                formed += 1
            
            #if we have formed a substr that has same chars as req
            while formed == req:
                cur_len = r - l + 1
                if cur_len < best:
                    best = cur_len
                    best_l = l
                #shrink window from left by decreasing that char in window_freq
                window_freq[s[l]] -= 1
                #after decr freq of l in map, if it does not match the req freq of the same char in t_freq; then we decr formed
                if s[l] in t_freq and window_freq[s[l]] < t_freq[s[l]]:
                    formed -= 1
                if window_freq[s[l]] == 0:
                    del window_freq[s[l]]
                l += 1

        if best == float("inf"):
            return ""
            
        return s[best_l:best_l + best]

        
        
                
    
        


