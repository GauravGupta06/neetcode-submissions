class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (1, len(nums)):
            j = i
            while j > 0 and (nums[j - 1] > nums[j]):
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp
                j -= 1
        for i in range (len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        return False