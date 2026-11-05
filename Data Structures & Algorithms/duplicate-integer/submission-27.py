class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alrSeen = set()
        for num in nums:
            if num in alrSeen:
                return True
            alrSeen.add(num)
        return False