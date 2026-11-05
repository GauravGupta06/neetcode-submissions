class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(' : ')', '{' : '}', '[' : ']'}

        mystack = []

        for b in s:
            if b in brackets:
                mystack.append(b)
            else:
                if (len(mystack) == 0):
                    return False
                curr = mystack.pop()
                if (brackets[curr] != b):
                    return False
        if (len(mystack) != 0):
            return False
        return True
                