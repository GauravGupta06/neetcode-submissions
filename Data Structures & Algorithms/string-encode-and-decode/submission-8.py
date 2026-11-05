class Solution:

    def encode(self, strs: List[str]) -> str:
        returnStr = ""
        for word in strs:
            returnStr += str(len(word)) + "#" + word
        
        return returnStr
        
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        returnList = []
        while j < len(s):
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1: j + 1 + length]
            returnList.append(word)
            j = j + 1 + length 
            i = j
        return returnList

        

        
