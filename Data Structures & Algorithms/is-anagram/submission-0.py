class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            hm_s[s[i]] = 1 + hm_s.get(s[i], 0)
            hm_t[t[i]] = 1 + hm_t.get(t[i], 0)
        return hm_s == hm_t
            
