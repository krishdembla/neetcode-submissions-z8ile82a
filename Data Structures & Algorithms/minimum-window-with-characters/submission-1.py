class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Base Case
        if t == "":
            return ""

        countT, window = {}, {}
        #iterate thru the chars of t and build frequency hashmap of chars in t
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need = 0, len(countT) #declaring have and need which tracks how many required chars from t we need to pass a substring in the sliding window as valid
        res, resLen = [-1, -1], float("infinity") #default values
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            #Add the newly encountered char only if it is in t and if we have not yet satisfied the required amount for this char
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # check if the current window which contains t, is smaller than the current best window
                if (r - l + 1) < resLen:
                    res = [l,r] #assign new res and resLen
                    resLen = r - l + 1

                window[s[l]] -= 1 #perform window shrink from the left
                #check if the window has now become invalid
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l,r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

                


