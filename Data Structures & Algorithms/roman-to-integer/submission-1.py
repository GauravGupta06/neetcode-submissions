class Solution:
    def romanToInt(self, s: str) -> int:
        myhash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0
        for x in range (len(s)):
            if (x < len(s) - 1):
                if (myhash[s[x]] < myhash[s[x+1]]):
                    sum -= myhash[s[x]]
                else:
                    sum += myhash[s[x]]
            else:
                sum += myhash[s[x]]
        return sum
            
                
                