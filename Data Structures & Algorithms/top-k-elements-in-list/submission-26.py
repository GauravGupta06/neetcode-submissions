class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        myTable = [[] for i in range (len(nums) + 1)]

        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1

        for num, frequency in hashTable.items():
            myTable[frequency].append(num)

        ret = []
        for i in range (len(nums), 0, -1):
            for number in myTable[i]:
                ret.append(number)
                if (len(ret) == k):
                    return ret
        


        


        
