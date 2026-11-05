class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range (len(nums)):
            num = nums[i]
            subtraction = target - num;
            if subtraction in hashTable:
                return [hashTable[subtraction], i]
            hashTable[num] = i