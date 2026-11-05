class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSubs = {} 

        for i in range(len(nums)):
            subValue = target - nums[i]
            if subValue in prevSubs:
                return [prevSubs[subValue], i]
            else:
                prevSubs[nums[i]] = i
        

        