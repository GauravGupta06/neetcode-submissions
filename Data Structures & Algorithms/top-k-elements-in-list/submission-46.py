class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap 
        # fill in hashmap with values and frequencies 
        # convert hashmap into tuple and sort 
        # pull top k keys 

        elements_freq = {}
        for num in nums:
            elements_freq[num] = elements_freq.get(num, 0) + 1
        
        sortedList = sorted(elements_freq.items(), key = lambda item: item[1])

        output = []
        # [[3, 3], [2, 2], [1, 1]]
        for idx in range(len(sortedList) - 1, len(sortedList) - 1 - k, -1):
            output.append(sortedList[idx][0])
        
        return output
            
