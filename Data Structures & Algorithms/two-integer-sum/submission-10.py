class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # subResult = target - nums[i]
        # check if subResult is in hash of previous subResults
        # if yes, then return that hash's value (index) + current index 
        # if not, then we append the hash table with nums[i] and i (its index)

        prevSubResults = {}
        for idx in range (len(nums)):
            subResult = target - nums[idx]
            if subResult in prevSubResults:
                return [prevSubResults[subResult], idx]
            else:
                prevSubResults[nums[idx]] = idx
        
        
        