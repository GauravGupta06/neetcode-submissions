class Solution:
    def isValid(self, s: str) -> bool:
        # create stack
        # loop through all letters in s
        # for each letter, check if its a open or closed bracket
        # if open bracket, push to stack
        # if closed, if stack is empty, return false. 
        #   else, pop value from list and check if letter == popped value. 
        #   if true, then continue, if false, return false. 

        # when while loop is done, if stack empty, return true, else return false. 

        myStack = []

        for letter in s:
            if (letter == '(' or letter ==  '{' or letter ==  '['):
                myStack.append(letter)
                continue
            else:
                if (len(myStack) == 0):
                    return False
                else:
                    popped = myStack.pop()
                    if (popped == '(' and letter == ')'):
                        continue
                    if (popped == '[' and letter == ']'):
                        continue
                    if (popped == '{' and letter == '}'):
                        continue
                    return False

        
        return (len(myStack) == 0)
                
                        

