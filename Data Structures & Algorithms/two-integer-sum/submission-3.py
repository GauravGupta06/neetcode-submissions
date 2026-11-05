class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            num1 = nums[x]
            for y in range(len(nums)):
                if y != x:
                    num2 = nums[y]
                    if num1 + num2 == target:
                        return [x, y]
                    



                