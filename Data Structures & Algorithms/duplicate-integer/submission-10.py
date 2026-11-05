class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            x = nums[i]
            for y in range (len(nums)):
                z = nums[y]
                if (y != i and z == x):
                    return True 
        return False
            

     