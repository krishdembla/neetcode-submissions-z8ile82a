class Solution:

    MAX_CHARS = 26

    def getHash(self, s):
        hashlist = [] #holds the complete hash code for a given string which will be converted to a string
        freq = [0] * self.MAX_CHARS #holds freq for a word of 26 possible chars where a is 0, b is 1 and so on

        for ch in s: #getting the freq of each char in the word by subtracting the ascii of that char with the min ascii of a
            freq[ord(ch) - ord('a')] += 1

        #loop to convert the list freq of hash values into a list string
        for i in range(self.MAX_CHARS):
            hashlist.append(str(freq[i]))
            hashlist.append("$")

        return ''.join(hashlist)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = {}
        for i in range(len(strs)): #iterate through len of the array strs
            key = self.getHash(strs[i])

            #checking to see if the key is present in the hm or not
            if(key not in mp):
                mp[key] = len(res) #a new group of anagrams has been encountered and is being added to the next index (len(res))
                res.append([])

            #if key exists we append the word to that group of anagrams in res
            res[mp[key]].append(strs[i])
        return res

    






            