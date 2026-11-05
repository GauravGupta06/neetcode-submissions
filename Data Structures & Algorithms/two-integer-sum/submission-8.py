class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i in range (len(nums)):
            subValue = target - nums[i]
            if subValue in hashTable:
                return [hashTable[subValue], i]
            else:
                hashTable[nums[i]] = i;
        