class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while (l < r):
            if (not self.alphaNum(s[l]) or not self.alphaNum(s[r])):
                if (not self.alphaNum(s[l])):
                    l += 1
                if (not self.alphaNum(s[r])):
                    r -= 1
                continue
            
            if (s[l].lower() != s[r].lower()):
                return False;
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
        ord('a') <= ord(char) <= ord('z') or 
        ord('0') <= ord(char) <= ord('9'))

        
        