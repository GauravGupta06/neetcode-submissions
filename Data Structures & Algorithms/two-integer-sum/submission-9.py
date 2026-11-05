class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i in range (len(nums)):
            num = nums[i]
            quotent = target - num
            if quotent in hashTable:
                return [hashTable[quotent], i] 
            else:
                hashTable[num] = i
            