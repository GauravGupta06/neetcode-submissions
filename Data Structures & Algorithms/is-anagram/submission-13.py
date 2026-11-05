class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CounterS = {}
        CounterT = {}
        for letter in s:
            CounterS[letter] = CounterS.get(letter, 0) + 1
        
        for letter in t:
            CounterT[letter] = CounterT.get(letter, 0) + 1
        
        newStr = s + t
        for letter in newStr:
            if CounterS.get(letter, 0) != CounterT.get(letter,0):
                return False
        return True
