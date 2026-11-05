class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySeen = []
        for num in nums:
            if num in alreadySeen:
                return True
            alreadySeen.append(num)
        return False 

