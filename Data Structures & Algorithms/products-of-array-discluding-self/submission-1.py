class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnList = []
        for i in range (len(nums)):
            value = 1
            for x in range (len(nums)):
                if x != i:
                    value *= nums[x]
            returnList.append(value)
        return returnList

            