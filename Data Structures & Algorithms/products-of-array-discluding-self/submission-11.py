class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = []
        postFix = []
        result = []

        multSoFar = 1

        for i in range (len(nums)):
            preFix.append(multSoFar)
            multSoFar *= nums[i]
        
        multSoFar = 1

        for i in range (len(nums) - 1, -1, -1):
            postFix.insert(0, multSoFar)
            multSoFar *= nums[i]

        for i in range(len(nums)):
            result.append(preFix[i] * postFix[i])
        
        return result
        

        
        



            

            