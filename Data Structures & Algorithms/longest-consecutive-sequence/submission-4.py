class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list into set so querying values is O(1) 
        # We create a list of all potential candidates 
        # For each potential candidate we query the set to see if a number greater than one of that candidate exists in a loop until we don't find another sequential number anymore, and if that number of iterations if greater than the rolling max then we repalce it. 
        # return the rolling max from step above. 

        nums_set = set(nums)

        potential_canidates = []
        for num in nums:
            if (num - 1 not in nums_set):
                potential_canidates.append(num)

        maxConsecutive = 0;

        for num in potential_canidates:
            currMax = 1;
            while (num + 1 in nums_set):
                currMax += 1
                num += 1
            if currMax > maxConsecutive:
                maxConsecutive = currMax

        return maxConsecutive

