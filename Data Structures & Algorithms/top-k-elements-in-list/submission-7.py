class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        output = []
        while k > 0:
            topKey = None
            topVal = float('-inf')
            for key, val in count.items():
                if val > topVal:
                    topVal = val
                    topKey = key 
            del count[topKey]
            output.append(topKey)
            k -= 1
        return output

