class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0): 
            return 0

        maxCounter = 1
        counter = 1
    
        for i in range (1, len(nums)):
            j = i
            while ((j > 0) and nums[j - 1] > nums [j]):
                temp = nums[j - 1] 
                nums[j - 1] = nums[j]
                nums[j] = temp
                j -= 1

        for i in range (len(nums) - 1):
            if (nums[i] + 1 == nums[i+1]):
                counter += 1
            elif (nums[i] != nums[i+1]):
                if (counter > maxCounter):
                    maxCounter = counter
                counter = 1
            
        if (counter > maxCounter):
            maxCounter = counter
        
        return maxCounter
            




            
            
                


        