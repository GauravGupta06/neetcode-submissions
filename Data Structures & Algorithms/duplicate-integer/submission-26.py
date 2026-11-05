class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1

        for value in hashTable.values():
            if value > 1:
                return True
        return False