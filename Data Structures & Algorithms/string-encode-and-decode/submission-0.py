class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        #trying to encode ["neet","code","love","you"] as:
        #"4#neet4#code4#love3#you"
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i #setting i value to j and iterating till # is reached
            while s[j] != '#': #loop and increment i till # delimiter is found
                j += 1
            length = int(s[i:j]) #chars from i to j is the len of a string
            i = j + 1 #setting new i to next char after pound found @ j
            j = i + length #i is now at start of the string so i + len
            res.append(s[i:j])
            i = j

        return res
